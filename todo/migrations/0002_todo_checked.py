# Generated by Django 4.0.6 on 2023-10-17 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]
