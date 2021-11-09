from django.contrib import admin
from .models import User, Book, Category
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Book)
admin.site.register(Category)
# Register your models here.
