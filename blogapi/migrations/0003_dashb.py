# Generated by Django 4.1.10 on 2023-11-12 11:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blogapi", "0002_blog_picurl"),
    ]

    operations = [
        migrations.CreateModel(
            name="dashb",
            fields=[
                ("dash_d_id", models.AutoField(primary_key=True, serialize=False)),
                ("view_d", models.IntegerField()),
                ("date_d", models.DateField()),
            ],
        ),
    ]
