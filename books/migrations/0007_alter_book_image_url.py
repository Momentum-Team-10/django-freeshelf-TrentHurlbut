# Generated by Django 3.2.9 on 2021-11-08 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_book_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image_url',
            field=models.URLField(null=True),
        ),
    ]