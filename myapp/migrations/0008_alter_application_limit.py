# Generated by Django 4.1.2 on 2023-02-10 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0007_remove_trackinghistory_limit_application_limit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="limit",
            field=models.CharField(
                blank=True, default="Not Updated Yet", max_length=100, null=True
            ),
        ),
    ]
