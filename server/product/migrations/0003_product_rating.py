# Generated by Django 2.2.2 on 2020-03-06 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
