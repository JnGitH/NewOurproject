# Generated by Django 2.1.2 on 2018-10-18 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelnote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tcontent',
            name='contentt',
            field=models.TextField(default='not have message'),
        ),
    ]
