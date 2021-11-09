from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

CATEGORIES = (
    ('game development', 'Game Development'), 
    ('cli', 'CLI'), 
    ('r', 'R'), 
    ('python', 'Python'), 
    ('javascript', 'JavaScript'), 
    ('html', 'HTML'), 
    ('css', 'CSS')
    )


class User(AbstractUser):

    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=200)
    book_url = models.URLField(unique=True)
    description = models.TextField()
    created_at = models.DateTimeField()
    image_url = models.URLField(blank=True, null=True)
    favorited = models.BooleanField(default=False)
    categories = models.ManyToManyField('Category', related_name='books')

    def publish(self):
        self.created_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Category(models.Model):
    name=models.CharField(max_length=16, choices=CATEGORIES, default=None, null=True)

    def __str__(self):
        return self.name
