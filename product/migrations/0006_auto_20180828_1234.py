# Generated by Django 2.1 on 2018-08-28 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20180828_1018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('-created', '-modified')},
        ),
    ]