# Generated by Django 4.0.4 on 2022-08-31 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_create_vouchermodels'),
    ]

    operations = [
        migrations.CreateModel(
            name='emp_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=225)),
                ('cat_alias', models.CharField(max_length=225)),
                ('revenue_items', models.CharField(max_length=225)),
                ('non_revenue_items', models.CharField(max_length=225)),
            ],
        ),
    ]
