# Generated by Django 3.2.9 on 2021-11-09 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_alter_book_book_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='favorited',
            field=models.BooleanField(default=False),
        ),
    ]
