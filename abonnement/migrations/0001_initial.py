# Generated by Django 2.2.28 on 2024-12-22 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abonnement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=200)),
                ('address', models.TextField(max_length=500)),
                ('email', models.TextField(max_length=50)),
                ('phone', models.TextField(max_length=20)),
            ],
        ),
    ]
