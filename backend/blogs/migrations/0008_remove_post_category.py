# Generated by Django 4.1.3 on 2022-12-10 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_category_alter_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
