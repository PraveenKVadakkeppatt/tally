# Generated by Django 4.0.4 on 2022-08-22 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_rename_base_cur_companies_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co_name', models.CharField(max_length=100, null=True)),
                ('maintain_acconts', models.CharField(max_length=100, null=True)),
                ('bill_wise_entry', models.CharField(max_length=100, null=True)),
                ('cost_centers', models.CharField(max_length=100, null=True)),
                ('interest_calc', models.CharField(max_length=100, null=True)),
                ('maintain_inventory', models.CharField(max_length=100, null=True)),
                ('integrate_accounts', models.CharField(max_length=100, null=True)),
                ('multiple_price_level', models.CharField(max_length=100, null=True)),
                ('batches', models.CharField(max_length=100, null=True)),
                ('expirydate_batches', models.CharField(max_length=100, null=True)),
                ('joborder_processing', models.CharField(max_length=100, null=True)),
                ('cost_tracking', models.CharField(max_length=100, null=True)),
                ('job_costing', models.CharField(max_length=100, null=True)),
                ('discount_invoices', models.CharField(max_length=100, null=True)),
                ('Billed_Quantity', models.CharField(max_length=100, null=True)),
                ('gst', models.CharField(max_length=100, null=True)),
                ('tds', models.CharField(max_length=100, null=True)),
                ('tcs', models.CharField(max_length=100, null=True)),
                ('vat', models.CharField(max_length=100, null=True)),
                ('excise', models.CharField(max_length=100, null=True)),
                ('servicetax', models.CharField(max_length=100, null=True)),
                ('payroll', models.CharField(max_length=100, null=True)),
                ('multiple_addrss', models.CharField(max_length=100, null=True)),
                ('vouchers', models.CharField(max_length=100, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies')),
            ],
        ),
        migrations.CreateModel(
            name='gst_taxability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxability', models.CharField(max_length=100, null=True)),
                ('integrated_tax', models.CharField(max_length=100, null=True)),
                ('cess', models.CharField(max_length=100, null=True)),
                ('flood_cess', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tds_person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('son_daughter', models.CharField(max_length=100, null=True)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('pan', models.CharField(max_length=100, null=True)),
                ('flat_no', models.CharField(max_length=100, null=True)),
                ('building', models.CharField(max_length=100, null=True)),
                ('street', models.CharField(max_length=100, null=True)),
                ('area', models.CharField(max_length=100, null=True)),
                ('town', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('pincode', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=100, null=True)),
                ('std', models.CharField(max_length=100, null=True)),
                ('telephone', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies')),
            ],
        ),
        migrations.RenameModel(
            old_name='tds',
            new_name='Tds_Details',
        ),
        migrations.RemoveField(
            model_name='feature_company',
            name='company',
        ),
        migrations.DeleteModel(
            name='gst_details_cmpny',
        ),
        migrations.RemoveField(
            model_name='tds_personal1',
            name='company',
        ),
        migrations.RenameField(
            model_name='gst',
            old_name='ad_rec',
            new_name='advance_receipts',
        ),
        migrations.RenameField(
            model_name='gst',
            old_name='appli_form',
            new_name='applicable_form',
        ),
        migrations.RenameField(
            model_name='gst',
            old_name='bill_frm',
            new_name='applicable_form1',
        ),
        migrations.RenameField(
            model_name='gst',
            old_name='e_way',
            new_name='assessee',
        ),
        migrations.RenameField(
            model_name='gst',
            old_name='einvoice',
            new_name='billfrom_place',
        ),
        migrations.RenameField(
            model_name='gst',
            old_name='gst_app_frm',
            new_name='bond_details',
        ),
        migrations.RenameField(
            model_name='gst',
            old_name='gst_class',
            new_name='e_invoice',
        ),
        migrations.RenameField(
            model_name='gst',
            old_name='gst_rate',
            new_name='gst_applicable',
        ),
        migrations.RenameField(
            model_name='gst',
            old_name='limit_in',
            new_name='gst_classification',
        ),
        migrations.RenameField(
            model_name='gst',
            old_name='lut_bnd',
            new_name='gst_rate_details',
        ),
        migrations.RenameField(
            model_name='gst',
            old_name='rev_chrg',
            new_name='gstin',
        ),
        migrations.RenameField(
            model_name='gst',
            old_name='snd_ewaybill',
            new_name='print_eway',
        ),
        migrations.RenameField(
            model_name='gst',
            old_name='tax_cal',
            new_name='reverse_charge',
        ),
        migrations.RenameField(
            model_name='gst',
            old_name='thr_limit',
            new_name='send_ewaybill',
        ),
        migrations.RenameField(
            model_name='gst',
            old_name='thre_limit',
            new_name='tax_calc',
        ),
        migrations.RenameField(
            model_name='gst',
            old_name='turnover',
            new_name='tax_rate',
        ),
        migrations.RenameField(
            model_name='gst',
            old_name='uin',
            new_name='threshold_includes',
        ),
        migrations.RenameField(
            model_name='tds_details',
            old_name='set_alt_details',
            new_name='person_details',
        ),
        migrations.RenameField(
            model_name='tds_details',
            old_name='tan_reg',
            new_name='tan',
        ),
        migrations.RenameField(
            model_name='tds_details',
            old_name='tax_colle',
            new_name='tan_regno',
        ),
        migrations.AddField(
            model_name='gst',
            name='threshold_limit',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='gst',
            name='threshold_limit2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='feature_company',
        ),
        migrations.DeleteModel(
            name='tds_personal1',
        ),
    ]