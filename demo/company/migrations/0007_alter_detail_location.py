# Generated by Django 4.0.8 on 2024-09-11 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_alter_detail_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='location',
            field=models.CharField(default='Unknown', max_length=255),
        ),
    ]
