# Generated by Django 3.1.1 on 2020-10-01 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_auto_20200930_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.post'),
        ),
    ]
