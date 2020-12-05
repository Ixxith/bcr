# Generated by Django 3.1.2 on 2020-11-19 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empfirst_name', models.CharField(max_length=30)),
                ('emplast_name', models.CharField(max_length=30)),
                ('empaddress', models.CharField(max_length=150)),
                ('empcity', models.CharField(max_length=150)),
                ('empstate', models.CharField(max_length=30)),
                ('empzip', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Paint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paintname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Zip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zipaddress', models.CharField(max_length=150)),
                ('zipstate', models.CharField(max_length=30)),
                ('zip', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtitle', models.CharField(max_length=30)),
                ('jobdescription', models.CharField(max_length=150)),
                ('estimatecost', models.CharField(max_length=15)),
                ('totalrevenue', models.CharField(max_length=15)),
                ('employee', models.ManyToManyField(blank=True, to='mainpages.Employee')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpages.zip')),
                ('paint', models.ManyToManyField(blank=True, to='mainpages.Paint')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_first_name', models.CharField(max_length=30)),
                ('contact_last_name', models.CharField(max_length=30)),
                ('contact_phone', models.CharField(max_length=30)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpages.zip')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('company_contact', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainpages.companycontact')),
            ],
        ),
    ]