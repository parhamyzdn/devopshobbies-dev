# Generated by Django 4.0.7 on 2023-07-08 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_baseuser_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='subscriber_count',
            new_name='subscribers_count',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='subscription_count',
            new_name='subscribings_count',
        ),
    ]