# Generated by Django 4.1.6 on 2023-02-28 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='likes',
            new_name='likecount',
        ),
    ]
