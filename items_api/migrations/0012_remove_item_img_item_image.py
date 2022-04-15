# Generated by Django 4.0.3 on 2022-04-15 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_api', '0011_alter_item_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='img',
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.CharField(default='https://i.imgur.com/3cHAFsx.jpg', max_length=2000),
        ),
    ]