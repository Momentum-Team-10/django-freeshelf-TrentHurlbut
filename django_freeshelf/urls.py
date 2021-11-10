"""django_freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from books import views
import debug_toolbar
from books.models import Category

admin.autodiscover()

urlpatterns = [
    path("", views.home_page, name = 'home_page'),
    path("admin/", admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/profile/', views.profile_page, name = 'profile_page'),
    path('books/add_books/', views.add_books, name = 'add_books'),
    path('books/<str:category>/', views.filter_by, name = 'filter_by'),
    path('books/edit/<int:pk>', views.edit_book, name = 'edit_book'),
    path('books/delete/<int:pk>', views.delete_book, name = 'delete_book'),
]
