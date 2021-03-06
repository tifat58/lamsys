# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-12 06:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0006_auto_20161204_1103'),
        ('leave', '0010_auto_20170313_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeLeaveSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency', models.IntegerField()),
                ('isActive', models.NullBooleanField()),
                ('isDelete', models.NullBooleanField()),
                ('insertUser', models.CharField(max_length=50)),
                ('insertDate', models.DateField(blank=True, null=True)),
                ('updateUser', models.CharField(max_length=50)),
                ('updateDate', models.DateField(blank=True, null=True)),
                ('project', models.CharField(max_length=100)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Employee')),
                ('leave_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leave.LeaveCategory')),
            ],
        ),
    ]
