# Generated by Django 3.2.9 on 2021-11-09 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_auto_20211109_1846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='category',
            new_name='categories',
        ),
    ]
