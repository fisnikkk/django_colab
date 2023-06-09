# Generated by Django 4.0.10 on 2023-03-24 10:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date.today),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='documents/%Y/%m/%d'),
        ),
    ]
