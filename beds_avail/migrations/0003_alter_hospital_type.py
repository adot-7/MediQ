# Generated by Django 5.1.1 on 2024-09-05 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beds_avail', '0002_alter_hospital_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='type',
            field=models.CharField(choices=[('government', 'Government'), ('private', 'Private')], max_length=255),
        ),
    ]
