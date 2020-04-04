# Generated by Django 3.0.5 on 2020-04-04 08:52

import common.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('offers', '0004_remove_clients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Product', max_length=255)),
                ('price', models.IntegerField(default=common.utils.get_default_price)),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='offers.Offer')),
            ],
        ),
    ]
