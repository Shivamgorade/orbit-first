# Generated by Django 4.2.2 on 2023-09-04 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orbitapp', '0003_quote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='text',
            field=models.TextField(max_length=100),
        ),
    ]
