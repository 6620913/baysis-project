# Generated by Django 4.1.7 on 2023-03-13 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authorization',
            fields=[
                ('reqID', models.CharField(max_length=30, primary_key='TRUE', serialize=False)),
                ('date', models.CharField(max_length=10)),
                ('urgency', models.CharField(max_length=50)),
                ('services', models.TextField()),
                ('requested_by', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
