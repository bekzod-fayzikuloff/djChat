# Generated by Django 3.2.6 on 2021-08-19 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_message_voice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Сообщение'),
        ),
    ]
