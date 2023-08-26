# Generated by Django 4.2.2 on 2023-08-25 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('apply_link', models.URLField()),
            ],
        ),
    ]
