# Generated by Django 3.1.7 on 2021-10-14 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ucnitk', '0006_auto_20211011_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=1),
        ),
    ]