from django.shortcuts import render
from .models import Book, Category
from django.contrib.auth.decorators import login_required
from .forms import BookForm
from django.shortcuts import redirect

def home_page(request):
  books = Book.objects.order_by('created_at')
  categories = Category.objects.all()
  return render(request, 'books/home_page.html', {"books":books, "categories":categories})

@login_required
def profile_page(request):
  user = request.user
  books = Book.objects.order_by('created_at')
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

def filter_by(request, category):
  books=Book.objects.filter(categories__name=category)
  return render(request, 'books/filtered_page.html', {"books":books, "category":category})
