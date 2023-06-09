# Generated by Django 4.0 on 2023-03-23 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_blogpost_delete_mymodel_remove_userprofile_birthdate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='pub_date',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
