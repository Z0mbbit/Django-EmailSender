# Generated by Django 5.0 on 2024-01-20 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailadress', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
