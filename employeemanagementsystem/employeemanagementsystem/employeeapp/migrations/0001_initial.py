# Generated by Django 5.0.6 on 2024-06-26 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("eid", models.AutoField(primary_key=True, serialize=False)),
                ("ename", models.CharField(max_length=200)),
                ("egender", models.CharField(max_length=200)),
                ("esalary", models.IntegerField()),
                ("eyoe", models.IntegerField()),
                ("edept", models.CharField(max_length=200)),
                ("ecompany", models.CharField(max_length=200)),
            ],
        ),
    ]
