# Generated by Django 4.1.7 on 2023-02-25 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='image',
            field=models.ImageField(default='Images/None/No0img.jpg', upload_to='Images/'),
        ),
    ]
