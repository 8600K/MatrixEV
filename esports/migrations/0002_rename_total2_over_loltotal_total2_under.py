# Generated by Django 5.0.1 on 2024-04-12 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("esports", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="loltotal", old_name="total2_over", new_name="total2_under",
        ),
    ]
