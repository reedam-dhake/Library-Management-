# Generated by Django 3.2 on 2021-04-15 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pages', models.CharField(max_length=5)),
                ('complete', models.BooleanField()),
                ('isbnNumber', models.CharField(max_length=13)),
                ('publisher', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=4)),
            ],
        ),
        migrations.RenameModel(
            old_name='ToDoList',
            new_name='BookName',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='details',
            name='bookName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.bookname'),
        ),
    ]
