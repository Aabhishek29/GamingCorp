# Generated by Django 4.0 on 2022-01-08 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('phNumber', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=15, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=15)),
                ('createdAt', models.DateField()),
            ],
        ),
    ]
