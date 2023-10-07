# Generated by Django 4.2.2 on 2023-10-02 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orbitapp', '0005_card_experience_card_qualification_card_salary_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Senior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
                ('expertise', models.CharField(max_length=100)),
                ('experience_years', models.IntegerField()),
                ('working_in', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='card',
            name='experience',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='card',
            name='qualification',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='card',
            name='salary',
            field=models.CharField(max_length=100),
        ),
    ]
