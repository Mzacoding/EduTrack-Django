# Generated by Django 5.1.6 on 2025-05-07 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edutrackApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='DepartmentCode',
            new_name='D_Code',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='DepartmentCode',
            new_name='D_Code',
        ),
    ]
