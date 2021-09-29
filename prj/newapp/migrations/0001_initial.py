# Generated by Django 3.2.7 on 2021-09-13 12:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0, 'Quantity should be >=0')])),
                ('price', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0, 'Quantity should be >=0')])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.category')),
            ],
        ),
    ]
