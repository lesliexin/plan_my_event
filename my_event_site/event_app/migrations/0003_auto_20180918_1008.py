# Generated by Django 2.1.1 on 2018-09-18 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0002_auto_20180918_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='title',
            field=models.CharField(default='', max_length=250),
        ),
    ]