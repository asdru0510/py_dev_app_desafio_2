# Generated by Django 5.1 on 2024-08-24 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("desafioadl", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subtarea",
            name="description",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="tarea",
            name="description",
            field=models.TextField(default=""),
        ),
    ]
