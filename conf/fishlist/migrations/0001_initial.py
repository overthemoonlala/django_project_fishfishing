# Generated by Django 4.0.6 on 2022-07-31 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Extinct',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
                ('reason', models.CharField(max_length=5000)),
                ('shape', models.CharField(max_length=5000)),
                ('ecology', models.CharField(max_length=5000)),
                ('place', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Nomal',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
                ('shape', models.CharField(max_length=5000)),
                ('ecology', models.CharField(max_length=5000)),
                ('place', models.CharField(max_length=5000)),
                ('eat', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Poison',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
                ('shape', models.CharField(max_length=5000)),
                ('ecology', models.CharField(max_length=5000)),
                ('place', models.CharField(max_length=5000)),
                ('eat', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('no', models.IntegerField(primary_key=True, serialize=False)),
                ('kind', models.CharField(max_length=150, null=True)),
                ('explain', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]
