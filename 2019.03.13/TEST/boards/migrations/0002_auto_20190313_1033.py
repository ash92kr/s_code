# Generated by Django 2.1.7 on 2019-03-13 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
