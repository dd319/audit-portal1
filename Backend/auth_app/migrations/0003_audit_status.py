# Generated by Django 5.0.7 on 2024-07-22 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_audit_check_status_audit_remarks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='audit',
            name='status',
            field=models.CharField(default='draft', max_length=10),
        ),
    ]