# Generated by Django 2.2.5 on 2020-03-13 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0011_notices_create_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lectors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=246)),
                ('file', models.FileField(upload_to='lectors')),
            ],
        ),
    ]
