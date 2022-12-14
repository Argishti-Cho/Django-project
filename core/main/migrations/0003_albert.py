# Generated by Django 4.1.2 on 2022-10-28 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_motorcicle_delete_cars'),
    ]

    operations = [
        migrations.CreateModel(
            name='Albert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='About Albert')),
                ('image', models.ImageField(upload_to='media', verbose_name='ImageField')),
            ],
            options={
                'verbose_name': 'Albert',
                'verbose_name_plural': 'Alberts',
                'ordering': ['name'],
            },
        ),
    ]
