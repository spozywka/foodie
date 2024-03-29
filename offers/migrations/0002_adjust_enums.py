# Generated by Django 3.0.5 on 2020-04-03 20:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='category',
            field=models.CharField(choices=[('Food', 'Food'), ('Drinks', 'Drinks'), ('Plants', 'Plants')], default='Food', max_length=255),
        ),
        migrations.AlterField(
            model_name='offer',
            name='city',
            field=models.CharField(choices=[('Warsaw', 'Warsaw'), ('Wroclaw', 'Wroclaw'), ('Cracow', 'Cracow'), ('Lodz', 'Lodz'), ('Szczecin', 'Szczecin')], default='Warsaw', max_length=255),
        ),
        migrations.AlterField(
            model_name='offer',
            name='delivery_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 4, 20, 46, 4, 881105)),
        ),
        migrations.AlterField(
            model_name='offer',
            name='distance',
            field=models.CharField(default='4.3 km from you', max_length=255),
        ),
        migrations.AlterField(
            model_name='offer',
            name='photo_url',
            field=models.CharField(default='https://images.unsplash.com/photo-1455099675745-a442989ac8bf?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=300&ixid=eyJhcHBfaWQiOjF9&ixlib=rb-1.2.1&q=80&w=400', max_length=2048),
        ),
    ]
