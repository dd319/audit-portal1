# Generated by Django 5.0.7 on 2024-07-19 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audit',
            name='check_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='audit',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='audit',
            name='remarks_for_operations',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='audit',
            name='sub_barcode',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='audit',
            name='audit_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='audit',
            name='case_error',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='audit',
            name='case_status',
            field=models.CharField(max_length=100),
        ),
    ]
