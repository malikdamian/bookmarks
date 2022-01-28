# Generated by Django 4.0.1 on 2022-01-20 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='user_like',
            new_name='users_like',
        ),
        migrations.AlterField(
            model_name='image',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]