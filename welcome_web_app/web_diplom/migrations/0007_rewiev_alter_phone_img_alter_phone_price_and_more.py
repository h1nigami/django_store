# Generated by Django 4.1.5 on 2023-06-20 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_diplom', '0006_alter_tarifs_description_alter_tarifs_description1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rewiev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('review', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='phone',
            name='img',
            field=models.ImageField(upload_to='static/img/'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tarifs',
            name='price',
            field=models.IntegerField(),
        ),
    ]
