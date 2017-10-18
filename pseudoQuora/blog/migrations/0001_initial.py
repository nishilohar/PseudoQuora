# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-04 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionAndAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=500)),
                ('answer', models.TextField()),
                ('askedBy', models.TextField(max_length=50)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
