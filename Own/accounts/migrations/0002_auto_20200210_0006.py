# Generated by Django 2.2.5 on 2020-02-09 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PizzaName', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='CarName',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='AgeofVehicle',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='ManuName',
            field=models.CharField(default=True, max_length=246),
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ToppingsName', models.CharField(max_length=100)),
                ('toppings', models.ManyToManyField(to='accounts.Topping')),
            ],
        ),
    ]
