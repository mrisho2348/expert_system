# Generated by Django 4.2.13 on 2024-07-08 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
