# Generated by Django 3.2.9 on 2021-11-08 22:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20211108_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 8, 22, 25, 38, 754736, tzinfo=utc)),
            preserve_default=False,
        ),
    ]