# Generated by Django 4.2.9 on 2024-01-05 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PsychoType',
            fields=[
                ('name', models.CharField(max_length=40, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('ptypes', models.ManyToManyField(to='testapp.psychotype')),
            ],
        ),
    ]
