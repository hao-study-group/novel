# Generated by Django 2.2 on 2019-04-07 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20190407_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='face',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='头像'),
        ),
    ]