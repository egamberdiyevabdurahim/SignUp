# Generated by Django 4.2.7 on 2023-11-03 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='1.jpg', upload_to='userphoto/'),
        ),
    ]