# Generated by Django 3.2.9 on 2021-11-09 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_remove_user_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(to='books.Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('game development', 'Game Development'), ('cli', 'CLI'), ('r', 'R'), ('python', 'Python'), ('javascript', 'JavaScript'), ('html', 'HTML'), ('css', 'CSS')], default=None, max_length=16, null=True),
        ),
    ]
