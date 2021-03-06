# Generated by Django 3.2 on 2021-04-21 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_comment_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookname',
            old_name='total_copies',
            new_name='waitlist',
        ),
        migrations.AlterField(
            model_name='bookname',
            name='isbnNumber',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bookname',
            name='pages',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bookname',
            name='year',
            field=models.IntegerField(),
        ),
    ]
