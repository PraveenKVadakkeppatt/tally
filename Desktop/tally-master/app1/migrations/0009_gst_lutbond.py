# Generated by Django 4.0.4 on 2022-08-20 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_gst_details_cmpny'),
    ]

    operations = [
        migrations.CreateModel(
            name='gst_lutbond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lutbond', models.CharField(max_length=100, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.create_companys')),
            ],
        ),
    ]
