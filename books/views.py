from django.shortcuts import render
from .models import Book, Category, User
from django.contrib.auth.decorators import login_required
from .forms import BookForm
from django.shortcuts import redirect, get_object_or_404

def home_page(request, pk=None):
  books = Book.objects.order_by('-created_at')
  current_user = request.user
  favorites = current_user.favorites.all()
  categories = Category.objects.all()
  if request.method == 'POST':
    current_user.favorites.add(pk=pk)
    return redirect('home_page')
  else:
    return render(request, 'books/home_page.html', {"books":books, "categories":categories, "favorites":favorites})

@login_required
def profile_page(request):
  user = request.user
  books = Book.objects.order_by('-created_at')
  return render(request, 'books/profile_page.html', {"books":books, "user":user})

def add_books(request):
  if request.method == 'POST':
    form = BookForm(request.POST)
    if form.is_valid():
      book = form.save(commit=False)
      book.publish()
      form.save_m2m()
      return redirect('home_page')
  else:
    form = BookForm()
  return render(request, 'books/add_books.html', {'form':form})

def filter_by(request, name):
  books=Book.objects.filter(categories__name=name)
  books.order_by('-created_at')
  return render(request, 'books/filtered_page.html', {"books":books, "category":name})

def edit_book(request, pk):
  book = get_object_or_404(Book, pk=pk)
  if request.method == "POST":
    form = BookForm(request.POST, instance=book)
    if form.is_valid():
      form.save()
      return redirect('home_page')
  else:
    form = BookForm(instance=book)
  return render(request, 'books/edit_book.html', {'form': form, 'book':book})

def delete_book(request, pk):
  book = get_object_or_404(Book, pk=pk)
  if request.method == "POST":
    book.delete()
    return redirect(to="home_page")

  return render(request, "books/delete_book.html", {"book": book})
