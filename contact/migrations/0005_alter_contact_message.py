# Generated by Django 3.2.7 on 2021-10-21 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_rename_created_at_contact_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=2000),
        ),
    ]
