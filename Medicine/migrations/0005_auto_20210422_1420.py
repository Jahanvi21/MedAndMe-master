# Generated by Django 3.1.6 on 2021-04-22 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medicine', '0004_alter_medicine_repeat_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='timing',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
