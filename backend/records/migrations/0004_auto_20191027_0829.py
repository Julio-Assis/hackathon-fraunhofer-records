# Generated by Django 2.2.6 on 2019-10-27 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_auto_20191027_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machinerecord',
            name='duration',
            field=models.CharField(max_length=50),
        ),
    ]
