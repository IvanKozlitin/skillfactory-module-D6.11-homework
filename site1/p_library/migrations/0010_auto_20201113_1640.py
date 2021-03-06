# Generated by Django 3.0.4 on 2020-11-13 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0009_book_friends'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterModelOptions(
            name='friend',
            options={'verbose_name': 'Друг', 'verbose_name_plural': 'Друзья'},
        ),
        migrations.AlterModelOptions(
            name='publishinghouse',
            options={'verbose_name': 'Издательство', 'verbose_name_plural': 'Издательства'},
        ),
        migrations.AlterModelOptions(
            name='whentook',
            options={'verbose_name': 'Книга у друга', 'verbose_name_plural': 'Книги у друзей'},
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to='books_images/%Y/%m/%d'),
        ),
    ]
