# Generated by Django 4.0.4 on 2022-08-20 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_gst_lutbond'),
    ]

    operations = [
        migrations.AddField(
            model_name='gst_lutbond',
            name='validity_from',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='gst_lutbond',
            name='validity_to',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
