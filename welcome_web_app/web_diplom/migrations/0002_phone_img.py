# Generated by Django 4.2.2 on 2023-06-15 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_diplom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='img',
            field=models.ImageField(default='/static/img/%Y/%m/%d/', upload_to='static/img/'),
        ),
    ]