# Generated by Django 2.0.7 on 2018-07-18 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_auto_20180718_1943'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='house',
            options={'verbose_name': 'тариф', 'verbose_name_plural': 'тарифы'},
        ),
        migrations.AlterField(
            model_name='house',
            name='price',
            field=models.IntegerField(verbose_name='цена'),
        ),
    ]
