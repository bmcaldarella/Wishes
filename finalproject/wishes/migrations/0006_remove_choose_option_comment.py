# Generated by Django 4.2.1 on 2023-08-22 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishes', '0005_choose_option_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choose_option',
            name='comment',
        ),
    ]
