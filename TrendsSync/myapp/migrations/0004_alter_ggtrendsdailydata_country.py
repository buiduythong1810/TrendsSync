# Generated by Django 5.0.6 on 2024-06-05 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_country_short_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ggtrendsdailydata',
            name='country',
            field=models.CharField(max_length=255),
        ),
    ]
