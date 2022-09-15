# Generated by Django 4.1 on 2022-09-09 03:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0002_alter_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='borrower',
            field=models.ForeignKey(blank=True, help_text='Выберите заказчика книги', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Заказчик'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(help_text='Выберите автора книги', null=True, to='catalog.author', verbose_name='Автор книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(help_text=' Выберите жанр для книги', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.genre', verbose_name='Жанр книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(help_text='Введите краткое описание книги', max_length=1000, verbose_name='Аннотация книги'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text=' Введите жанр книги', max_length=200, verbose_name='Жанр книги'),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(help_text=' Введите язык книги', max_length=20, verbose_name='Язык книги'),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(help_text='Введите статус экземпляра книги', max_length=20, verbose_name='Статус экземпляра книги'),
        ),
    ]