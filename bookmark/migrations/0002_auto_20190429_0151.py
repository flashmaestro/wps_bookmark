# Generated by Django 2.2 on 2019-04-29 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmark',
            options={'ordering': ['site_name']},
        ),
    ]
