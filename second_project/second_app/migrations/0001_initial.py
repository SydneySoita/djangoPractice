# Generated by Django 3.2.5 on 2022-05-09 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=254, unique=True)),
                ('lastname', models.CharField(max_length=254, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]