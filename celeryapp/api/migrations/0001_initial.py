# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identify', models.CharField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=4, max_digits=14)),
            ],
        ),
        migrations.CreateModel(
            name='GetData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identify', models.CharField(max_length=20)),
                ('is_disabled', models.BooleanField(default=False)),
                ('amount', models.DecimalField(decimal_places=4, max_digits=14)),
                ('last_payment', models.DateTimeField(blank=True, null=True)),
                ('next_payment', models.DateTimeField(blank=True, null=True)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]