# Generated by Django 3.2.22 on 2023-10-26 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forus_Webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='empreg1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=60)),
                ('rpassword', models.CharField(max_length=60)),
                ('dob', models.CharField(max_length=60)),
                ('gender', models.CharField(max_length=60)),
                ('phno', models.CharField(max_length=60)),
            ],
        ),
    ]
