# Generated by Django 4.1.2 on 2022-10-07 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['timestamp'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterModelOptions(
            name='contactprofile',
            options={'ordering': ['timestamp'], 'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AlterModelOptions(
            name='portfolio',
            options={'ordering': ['name'], 'verbose_name': 'Портфолио', 'verbose_name_plural': 'Проекты'},
        ),
    ]
