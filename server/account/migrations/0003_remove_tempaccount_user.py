# Generated by Django 2.2.2 on 2020-02-14 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_tempaccount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tempaccount',
            name='user',
        ),
    ]
