# Generated by Django 3.1.1 on 2020-09-22 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_auto_20200921_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='fecha_creación',
            field=models.DateField(default='2020-09-22'),
        ),
    ]
