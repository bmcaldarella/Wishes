# Generated by Django 4.2.1 on 2023-08-16 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishes', '0002_alter_user_groups_alter_user_user_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_vote',
            name='closingVote',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]