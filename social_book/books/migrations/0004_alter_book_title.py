# Generated by Django 5.1 on 2024-08-19 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0003_alter_book_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="title",
            field=models.CharField(max_length=255),
        ),
    ]
