# Generated by Django 4.2.2 on 2023-10-02 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orbitapp', '0006_senior_alter_card_experience_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='senior',
            name='picture',
            field=models.ImageField(default=0, upload_to='senior_pictures/'),
        ),
    ]
