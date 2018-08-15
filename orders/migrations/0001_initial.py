# Generated by Django 2.0.7 on 2018-08-02 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('houses', '0005_auto_20180802_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='имя')),
                ('phone', models.CharField(max_length=50, verbose_name='телефон')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='дата')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.House', verbose_name='тариф')),
            ],
        ),
    ]