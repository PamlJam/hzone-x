# Generated by Django 2.1.5 on 2021-03-25 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210325_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atc',
            name='toc',
            field=models.TextField(default='<div class="toc"><ul></ul></div>'),
        ),
    ]
