# Generated by Django 4.0.1 on 2023-10-31 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('name', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
                ('warenty', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
