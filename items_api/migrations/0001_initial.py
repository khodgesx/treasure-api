# Generated by Django 4.0.3 on 2022-04-08 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('category', models.CharField(max_length=40)),
                ('details', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('available', models.BooleanField()),
            ],
        ),
    ]
