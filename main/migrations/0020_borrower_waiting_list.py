# Generated by Django 3.2 on 2021-04-21 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20210421_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrower',
            name='waiting_list',
            field=models.BooleanField(default=False),
        ),
    ]
