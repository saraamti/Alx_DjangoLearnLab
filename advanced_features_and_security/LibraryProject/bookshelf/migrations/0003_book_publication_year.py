# Generated by Django 5.1.3 on 2024-11-21 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0002_alter_book_options_remove_book_publication_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publication_year',
            field=models.IntegerField(default=2000),
        ),
    ]