# Generated by Django 2.2.6 on 2019-10-25 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MachineRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('stop_timestamp', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('operator_timestamp', models.DateTimeField()),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='records.Machine')),
            ],
        ),
        migrations.CreateModel(
            name='CauseRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extras', models.CharField(max_length=200)),
                ('cause', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='records.Cause')),
                ('machine_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='causes', to='records.MachineRecord')),
            ],
        ),
    ]
