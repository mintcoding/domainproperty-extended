# Generated by Django 2.1.5 on 2019-02-20 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extendedsearch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SortKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_choices', models.CharField(choices=[('Default', 'Default'), ('Price', 'Price'), ('DateUpdated', 'Date Updated')], default='Default', max_length=20)),
            ],
        ),
    ]