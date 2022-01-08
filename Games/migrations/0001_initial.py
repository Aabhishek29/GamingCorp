# Generated by Django 4.0 on 2022-01-08 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyGames',
            fields=[
                ('GameName', models.CharField(max_length=30)),
                ('GameId', models.IntegerField(primary_key=True, serialize=False)),
                ('createdAt', models.DateField()),
                ('updatedAt', models.DateField()),
                ('Url', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
