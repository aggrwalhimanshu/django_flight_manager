# Generated by Django 2.2.5 on 2021-01-25 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_auto_20210125_1206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='airport',
            old_name='cite',
            new_name='city',
        ),
    ]
