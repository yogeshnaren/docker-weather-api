# Generated by Django 2.0.2 on 2018-02-27 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20180225_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weather',
            name='id',
        ),
        migrations.AlterField(
            model_name='weather',
            name='date',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]