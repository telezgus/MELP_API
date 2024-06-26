# Generated by Django 5.0.4 on 2024-05-02 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('name', models.TextField()),
                ('site', models.TextField()),
                ('email', models.TextField()),
                ('phone', models.TextField()),
                ('street', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
    ]
