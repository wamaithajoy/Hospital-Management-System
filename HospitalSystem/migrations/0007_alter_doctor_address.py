# Generated by Django 4.1.2 on 2022-10-19 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalSystem', '0006_appointmnet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='address',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
