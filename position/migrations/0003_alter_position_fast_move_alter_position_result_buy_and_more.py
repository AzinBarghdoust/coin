# Generated by Django 4.1.3 on 2022-12-10 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0002_position_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='fast_move',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='result_buy',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='result_sell',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='slow_move',
            field=models.IntegerField(null=True),
        ),
    ]
