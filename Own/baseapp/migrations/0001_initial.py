# Generated by Django 2.2.5 on 2020-02-11 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('church_pic', models.ImageField(blank=True, upload_to='church_pics')),
            ],
        ),
    ]
