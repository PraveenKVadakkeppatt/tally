# Generated by Django 4.0.4 on 2022-08-20 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_tally_ledger_group_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='gst_details_cmpny',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Taxability', models.CharField(max_length=100, null=True)),
                ('Integrated_Tax', models.CharField(max_length=100, null=True)),
                ('Cess', models.CharField(max_length=100, null=True)),
                ('Flood_Cess', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
