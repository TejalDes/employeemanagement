# Generated by Django 4.1.1 on 2022-09-12 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("employee", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PayRoll",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_of_joining", models.DateField()),
                ("salary", models.FloatField()),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employee.employee",
                    ),
                ),
            ],
        ),
    ]
