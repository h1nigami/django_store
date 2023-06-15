# Generated by Django 4.2.2 on 2023-06-15 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_diplom', '0002_phone_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='phone',
            name='img',
            field=models.ImageField(upload_to='web_diplom/static/img/'),
        ),
    ]