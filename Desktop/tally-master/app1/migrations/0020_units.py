# Generated by Django 4.0.4 on 2022-08-30 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_rounding_gratuity_compute_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='units',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=225)),
                ('symbol', models.CharField(max_length=225)),
                ('formal_name', models.CharField(max_length=225)),
                ('number_of_decimal_places', models.CharField(max_length=225)),
                ('first_unit', models.CharField(max_length=225)),
                ('conversion', models.CharField(max_length=225)),
                ('second_unit', models.CharField(max_length=225)),
            ],
        ),
    ]
