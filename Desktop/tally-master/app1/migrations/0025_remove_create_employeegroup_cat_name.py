# Generated by Django 4.0.4 on 2022-09-02 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0024_create_employeegroup_cat_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='create_employeegroup',
            name='cat_name',
        ),
    ]
