# Generated by Django 4.1.2 on 2022-10-19 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalSystem', '0003_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='address',
            field=models.TextField(max_length=20, null=True),
        ),
    ]