# Generated by Django 2.1.5 on 2021-03-12 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210312_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='motto',
            field=models.TextField(default='nothing at all', max_length=24),
        ),
    ]