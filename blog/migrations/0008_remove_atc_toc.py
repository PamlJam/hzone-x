# Generated by Django 2.1.5 on 2021-03-26 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210325_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atc',
            name='toc',
        ),
    ]
