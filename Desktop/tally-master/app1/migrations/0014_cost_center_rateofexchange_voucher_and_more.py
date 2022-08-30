# Generated by Django 4.0.4 on 2022-08-22 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_features_gst_taxability_tds_person_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='cost_center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=255)),
                ('cost_alias', models.CharField(max_length=255)),
                ('under', models.CharField(max_length=255)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies')),
            ],
        ),
        migrations.CreateModel(
            name='rateofexchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ROE', models.CharField(default='null', max_length=255)),
                ('currencyName', models.CharField(default='null', max_length=255)),
                ('stdrate', models.CharField(default='null', max_length=255)),
                ('sell_voucher_rate', models.CharField(default='null', max_length=255)),
                ('sell_specified_rate', models.CharField(default='null', max_length=255)),
                ('buy_voucher_rate', models.CharField(default='null', max_length=255)),
                ('buy_specified_rate', models.CharField(default='null', max_length=255)),
                ('currencyAlteration', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.currencyalteration')),
            ],
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voucher_name', models.CharField(max_length=255)),
                ('alias', models.CharField(max_length=255)),
                ('voucher_type', models.CharField(max_length=255)),
                ('abbreviation', models.CharField(max_length=255)),
                ('voucherActivate', models.CharField(max_length=255)),
                ('voucherNumber', models.CharField(max_length=255)),
                ('preventDuplicate', models.CharField(max_length=255)),
                ('advance_con', models.CharField(max_length=255)),
                ('voucherEffective', models.CharField(max_length=255)),
                ('transaction', models.CharField(max_length=255)),
                ('make_optional', models.CharField(max_length=255)),
                ('voucherNarration', models.CharField(max_length=255)),
                ('provideNarration', models.CharField(max_length=255)),
                ('journal', models.CharField(default='null', max_length=255)),
                ('purchase', models.CharField(max_length=255)),
                ('allocation', models.CharField(max_length=255)),
                ('printVoucher', models.CharField(max_length=255)),
                ('jurisdiction', models.CharField(default='null', max_length=255)),
                ('POSInvoice', models.CharField(max_length=255)),
                ('message1', models.CharField(max_length=255)),
                ('message2', models.CharField(max_length=255)),
                ('defaultBank', models.CharField(max_length=255)),
                ('titlePrint', models.CharField(max_length=255)),
                ('setAlter', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='cost_create',
            name='company',
        ),
        migrations.RemoveField(
            model_name='rate_exchange',
            name='currencyAlteration',
        ),
        migrations.DeleteModel(
            name='VoucherAlteration',
        ),
        migrations.DeleteModel(
            name='cost_create',
        ),
        migrations.DeleteModel(
            name='rate_exchange',
        ),
    ]
