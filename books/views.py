from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import login_required
from .forms import BookForm
from django.shortcuts import redirect

def home_page(request):
  books = Book.objects.order_by('created_at')
  return render(request, 'books/home_page.html', {"books":books})

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
      return redirect('home_page')
  else:
    form = BookForm()
  return render(request, 'books/add_books.html', {'form':form})
