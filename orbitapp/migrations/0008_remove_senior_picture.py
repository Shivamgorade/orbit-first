# Generated by Django 4.2.2 on 2023-10-02 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orbitapp', '0007_senior_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='senior',
            name='picture',
        ),
    ]