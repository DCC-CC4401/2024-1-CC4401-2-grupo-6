# Generated by Django 3.2.25 on 2024-07-10 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_tarea_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bathroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('building', models.CharField(max_length=3)),
                ('floor', models.IntegerField()),
                ('gender', models.CharField(choices=[('mujer', 'Mujer'), ('hombre', 'Hombre'), ('universal', 'Universal')], max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='tarea',
            name='fecha_creación',
            field=models.DateField(default='2024-07-10'),
        ),
    ]
