# Generated by Django 3.2.5 on 2021-07-28 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=254)),
                ('model', models.CharField(max_length=254)),
                ('year', models.CharField(max_length=254)),
                ('version', models.CharField(max_length=254)),
                ('enginecode', models.CharField(max_length=254)),
                ('fuel', models.CharField(max_length=254)),
                ('kw', models.CharField(max_length=254)),
                ('ecubrand', models.CharField(max_length=254)),
                ('ecuversion', models.CharField(max_length=254)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
