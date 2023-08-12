# Generated by Django 4.2 on 2023-07-20 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinic_name', models.CharField(blank=True, max_length=100, null=True)),
                ('clinic_address', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nurse_name', models.CharField(blank=True, max_length=100, null=True)),
                ('nurse_edu', models.CharField(blank=True, max_length=100, null=True)),
                ('nurse_address', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_name', models.CharField(blank=True, max_length=100, null=True)),
                ('provider_edu', models.CharField(blank=True, max_length=100, null=True)),
                ('provider_address', models.CharField(blank=True, max_length=100, null=True)),
                ('clinic_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clinic_app.clinic')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(blank=True, max_length=100, null=True)),
                ('patient_edu', models.CharField(blank=True, max_length=100, null=True)),
                ('patient_address', models.CharField(blank=True, max_length=100, null=True)),
                ('looked_by_nurse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clinic_app.nurse')),
            ],
        ),
        migrations.AddField(
            model_name='nurse',
            name='works_for_provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clinic_app.provider'),
        ),
    ]