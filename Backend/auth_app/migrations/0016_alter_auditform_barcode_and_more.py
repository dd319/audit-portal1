# Generated by Django 5.0.8 on 2024-08-07 06:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0015_alter_componentwitherror_sub_barcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditform',
            name='barcode',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='componentwithouterror',
            name='sub_barcode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fileattachment',
            name='component_with_error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='auth_app.componentwitherror'),
        ),
        migrations.AlterField(
            model_name='fileattachment',
            name='error_case',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='auth_app.errorcase'),
        ),
    ]
