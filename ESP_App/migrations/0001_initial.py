# Generated by Django 4.1.4 on 2022-12-08 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ESP_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(null=True)),
                ('humidity', models.FloatField(null=True)),
                ('save_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
