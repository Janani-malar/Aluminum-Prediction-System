# Generated by Django 4.0.8 on 2024-09-25 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_alter_detail_alumina_alter_detail_aluminum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='alumina',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='detail',
            name='aluminum',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='detail',
            name='bauxite',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='detail',
            name='carbonanodes',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='detail',
            name='causticsoda',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='detail',
            name='cryolite',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='detail',
            name='electricity',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='detail',
            name='lime',
            field=models.CharField(max_length=20),
        ),
    ]
