# Generated by Django 2.2.5 on 2020-02-29 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0004_post_create_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile_pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PPName', models.CharField(max_length=246)),
                ('Parishpriest_pic', models.ImageField(blank=True, upload_to='profile')),
                ('APName', models.CharField(max_length=246)),
                ('AsstPriest_pic', models.ImageField(blank=True, upload_to='profile')),
                ('AP2Name', models.CharField(max_length=246)),
                ('AsstPriest2_pic', models.ImageField(blank=True, upload_to='profile')),
            ],
        ),
    ]
