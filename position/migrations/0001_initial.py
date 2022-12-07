# Generated by Django 4.1.3 on 2022-11-27 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('cross moving average', 'cross moving average'), ('Cma + RSI + MACD', 'Cma + RSI + MACD')], max_length=30, null=True)),
                ('pair1', models.CharField(choices=[('BTC', 'BTC'), ('ETH', 'ETH')], max_length=3, null=True)),
                ('pair2', models.CharField(choices=[('USDT', 'USDT')], max_length=4, null=True)),
                ('time_frame', models.CharField(choices=[('min', 'min'), ('hour', 'hour'), ('day', 'day'), ('week', 'week')], max_length=4, null=True)),
                ('trade', models.CharField(choices=[('sell', 'sell'), ('buy', 'buy')], max_length=4, null=True)),
                ('slow_move', models.IntegerField()),
                ('fast_move', models.IntegerField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('operator', models.CharField(choices=[('Greater than', '>'), ('Less than', '<'), ('Greater than or equal to', '>='), ('Less than or equal to', '<='), ('Equal', '=')], max_length=25, null=True)),
                ('result_sell', models.FloatField()),
                ('result_buy', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
