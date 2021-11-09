from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import login_required

def home_page(request):
  books = Book.objects.order_by('created_at')
  return render(request, 'books/home_page.html', {"books":books})

@login_required
def profile_page(request):
  books = Book.objects.order_by('created_at')
  return render(request, 'books/profile_page.html', {"books":books})
