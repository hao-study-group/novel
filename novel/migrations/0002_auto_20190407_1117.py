# Generated by Django 2.2 on 2019-04-07 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novelcol',
            name='novel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='novel.NovelModel', verbose_name='关联小说'),
        ),
    ]
