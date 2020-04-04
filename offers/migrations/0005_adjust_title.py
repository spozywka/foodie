# Generated by Django 3.0.5 on 2020-04-04 09:20

import common.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0004_remove_clients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='title',
            field=models.CharField(default=common.utils.get_default_offer_title, max_length=255),
        ),
    ]
