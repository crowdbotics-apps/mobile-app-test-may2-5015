# Generated by Django 2.2.12 on 2020-05-27 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_load_initial_data"),
    ]

    operations = [
        migrations.AddField(
            model_name="customtext",
            name="new_field",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
