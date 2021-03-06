# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-21 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_remove_article_click_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '用户',
                'ordering': ['-id'],
                'verbose_name_plural': '用户',
            },
        ),
    ]
