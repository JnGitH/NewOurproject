# Generated by Django 2.1.2 on 2018-10-18 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategy', '0004_auto_20181018_0926'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='nofile')),
            ],
        ),
    ]
