# Generated by Django 5.1.6 on 2025-04-12 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edutrackApp', '0002_student_contactnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='contactNumber',
            field=models.CharField(max_length=20),
        ),
    ]
