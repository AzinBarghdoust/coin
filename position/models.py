from django.db import models
from accounts.models import User

TYPE = [
    ('cross moving average', 'cross moving average'),
    ('Cma + RSI + MACD', 'Cma + RSI + MACD')
]

PAIR1 = [
    ('BTC', 'BTC'),
    ('ETH', 'ETH')
]

PAIR2 = [
    ('USDT', 'USDT')
]

TIMEFRAME = [
    ('min', 'min'),
    ('hour', 'hour'),
    ('day', 'day'),
    ('week', 'week')
]
TIMEFRAME_NUM = [
    ('1', '1'),
    ('3', '3'),
    ('5', '5'),
    ('15', '15'),
    ('30', '30'),
    ('2', '2'),
    ('4', '4'),
    ('6', '6'),
    ('8', '8'),
    ('12', '12'),

]


TRADE = [
    ('sell', 'sell'),
    ('buy', 'buy')
]

OPERATOR = [
    ('Greater than', '>'),
    ('Less than', '<'),
    ('Greater than or equal to', '>='),
    ('Less than or equal to', '<='),
    ('Equal', '='),
]

STATUS = [
    ('active', 'active'),
    ('not active', 'not active'),
]


class Position(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=30, choices=TYPE, null=True)
    pair1 = models.CharField(max_length=3, choices=PAIR1, null=True)
    pair2 = models.CharField(max_length=4, choices=PAIR2, null=True)
    time_frame = models.CharField(max_length=4, choices=TIMEFRAME, null=True)
    trade = models.CharField(max_length=4, choices=TRADE, null=True)
    slow_move = models.IntegerField(null=True)
    fast_move = models.IntegerField(null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    operator = models.CharField(max_length=25, choices=OPERATOR, null=True)
    result_sell = models.FloatField(null=True)
    result_buy = models.FloatField(null=True)
    status = models.CharField(max_length=12, choices=STATUS, null=True, default='active')
    timeframe_num = models.IntegerField(null=True, choices=TIMEFRAME_NUM, default='1')
