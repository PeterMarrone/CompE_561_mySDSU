# Generated by Django 4.1.3 on 2022-12-05 07:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='applyToGrad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30, verbose_name='First Name')),
                ('lastName', models.CharField(max_length=50, verbose_name='Last Name')),
                ('redID', models.CharField(max_length=9, verbose_name='RedID')),
                ('catalogYear', models.CharField(max_length=4, verbose_name='Catalog Year')),
                ('major', models.CharField(max_length=100, verbose_name='Major')),
            ],
        ),
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redID', models.CharField(max_length=9, verbose_name='RedID')),
                ('advisor', models.CharField(max_length=100, verbose_name='Advisor')),
            ],
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseNumber', models.CharField(max_length=100, verbose_name='Course Number')),
                ('courseName', models.CharField(max_length=100, verbose_name='Course Name')),
                ('units', models.CharField(max_length=100, verbose_name='Units')),
                ('grade', models.CharField(max_length=100, verbose_name='Grade Recieved')),
                ('gpa', models.CharField(max_length=100, verbose_name='GPA')),
                ('semester', models.CharField(max_length=100, verbose_name='Semester')),
                ('students', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseNumber', models.CharField(max_length=100, verbose_name='Course Number')),
                ('courseName', models.CharField(max_length=100, verbose_name='Course Name')),
                ('units', models.CharField(max_length=100, verbose_name='Units')),
                ('dayAndTime', models.CharField(max_length=100, verbose_name='Day / Time')),
                ('location', models.CharField(max_length=100, verbose_name='Location')),
                ('semester', models.CharField(max_length=100, verbose_name='Semester')),
                ('students', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]