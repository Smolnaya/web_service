# Generated by Django 3.2.8 on 2021-10-30 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20211024_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(blank=True, choices=[('Игры', 'Игры'), ('ОС', 'ОС')], default='', max_length=100),
        ),
    ]