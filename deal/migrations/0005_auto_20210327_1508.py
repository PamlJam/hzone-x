# Generated by Django 2.1.5 on 2021-03-27 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0004_auto_20210327_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='item',
            name='info',
            field=models.TextField(max_length=50),
        ),
    ]