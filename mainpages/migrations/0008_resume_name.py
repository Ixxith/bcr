# Generated by Django 3.1.2 on 2020-12-08 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpages', '0007_auto_20201208_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='name',
            field=models.CharField(default='resume', max_length=100),
            preserve_default=False,
        ),
    ]