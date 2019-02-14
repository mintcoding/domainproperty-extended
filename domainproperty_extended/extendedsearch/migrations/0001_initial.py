# Generated by Django 2.1.5 on 2019-02-14 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DomainPropertyCache',
            fields=[
                ('cache_key', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=250)),
                ('expires', models.DateTimeField(db_index=True, max_length=250)),
            ],
        ),
    ]
