# Generated by Django 2.2.5 on 2020-02-12 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0002_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
    ]
