# Generated by Django 3.2 on 2021-04-19 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210419_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookname',
            name='summary',
            field=models.TextField(default=0, help_text='Enter a brief description of the book', max_length=1000),
            preserve_default=False,
        ),
    ]
