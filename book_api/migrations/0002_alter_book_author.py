# Generated by Django 4.1.7 on 2023-03-15 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default='D. G.', on_delete=django.db.models.deletion.CASCADE, to='book_api.author'),
        ),
    ]
