# Generated by Django 4.1.3 on 2022-12-25 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0003_alter_position_fast_move_alter_position_result_buy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='timeframe_num',
            field=models.IntegerField(choices=[('1', '1'), ('3', '3'), ('5', '5'), ('15', '15'), ('30', '30'), ('2', '2'), ('4', '4'), ('6', '6'), ('8', '8'), ('12', '12')], default='1', null=True),
        ),
    ]