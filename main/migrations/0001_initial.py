# Generated by Django 3.0.6 on 2020-06-06 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='products/images')),
                ('category', models.CharField(choices=[('LR', 'Rayonnages lourds'), ('MI', 'Rayonnages mi-lourd'), ('LG', 'Rayonnages léger'), ('PR', 'Protection'), ('AC', 'Accessoires')], max_length=2)),
            ],
        ),
    ]
