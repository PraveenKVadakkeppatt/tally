# Generated by Django 4.0.4 on 2022-08-30 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_create_payhead_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rounding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rounding_Method', models.CharField(blank=True, default='Null', max_length=225)),
                ('Round_limit', models.CharField(blank=True, default='Null', max_length=22)),
                ('pay_head_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.create_payhead')),
            ],
        ),
        migrations.CreateModel(
            name='gratuity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_of_months', models.CharField(max_length=225)),
                ('number_of_months_from', models.CharField(max_length=225)),
                ('to', models.CharField(max_length=225)),
                ('calculation_per_year', models.CharField(max_length=225)),
                ('pay_head_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.create_payhead')),
            ],
        ),
        migrations.CreateModel(
            name='compute_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compute', models.CharField(default='Null', max_length=225)),
                ('effective_from', models.CharField(default='NULL', max_length=225)),
                ('amount_greater', models.CharField(default='NULL', max_length=225)),
                ('amount_upto', models.CharField(default='NULL', max_length=225)),
                ('slab_type', models.CharField(default='NULL', max_length=225)),
                ('value', models.CharField(default='NULL', max_length=225)),
                ('Pay_head_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.create_payhead')),
            ],
        ),
    ]
