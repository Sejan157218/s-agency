# Generated by Django 3.1.2 on 2021-01-22 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testomonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('date', models.CharField(max_length=20)),
                ('image', models.ImageField(default='', upload_to='blog/images')),
            ],
        ),
    ]
