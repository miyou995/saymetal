# Generated by Django 3.0.6 on 2020-06-06 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
