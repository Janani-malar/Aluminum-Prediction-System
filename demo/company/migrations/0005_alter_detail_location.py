# Generated by Django 4.0.8 on 2024-09-11 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
