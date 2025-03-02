# Generated by Django 5.1.6 on 2025-02-23 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200, verbose_name='Product Name')),
                ('description', models.TextField(max_length=300, verbose_name='Product Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Product Price')),
                ('available', models.BooleanField(default=True, verbose_name='Product Availability')),
                ('photo', models.ImageField(null=True, upload_to='logos', verbose_name='Product Photo')),
            ],
        ),
    ]
