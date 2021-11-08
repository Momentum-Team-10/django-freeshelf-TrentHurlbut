from django.shortcuts import render
from .models import Book

def home_page(request):
  books = Book.objects.order_by('created_at')
  return render(request, 'books/home_page.html', {"books":books})
