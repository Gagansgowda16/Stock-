# Generated by Django 3.0.7 on 2023-11-18 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forus_Webapp', '0013_remove_deviceitem_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceitem',
            name='device_id',
            field=models.CharField(default=1, max_length=60),
        ),
    ]
