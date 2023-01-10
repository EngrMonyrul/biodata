# Generated by Django 4.1.4 on 2023-01-07 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.FloatField()),
                ('number', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='images')),
                ('details', models.TextField()),
            ],
        ),
    ]
