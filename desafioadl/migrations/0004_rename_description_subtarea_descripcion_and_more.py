# Generated by Django 5.1 on 2024-08-24 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("desafioadl", "0003_alter_subtarea_tarea_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="subtarea",
            old_name="description",
            new_name="descripcion",
        ),
        migrations.RenameField(
            model_name="tarea",
            old_name="description",
            new_name="descripcion",
        ),
    ]
