# Generated by Django 3.1.2 on 2021-01-19 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_admin_team_team'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin_team',
        ),
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
