import threading
import time
import schedule
from celery.schedules import crontab
from django.contrib.sites import requests
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from position.serializers import *
import requests
from position.models import Position
from datetime import datetime, date, timedelta
import pandas as pd
from threading import Timer


class PositionList(APIView):
    def get_queryset(self):
        position = Position.objects.filter(status='active')
        serializer = PositionSerializer(position, many=True)
        return Response({'data': serializer.data})


class CreatePosition(APIView):
    permission_classes = [IsAuthenticated]

    def check_sma(self, s, f):
        # timer = Timer(2, self.check_sma, args=(s, f))
        # timer.start()
        if s > f:

            print(True)
            return True
        else:

            print(False)
            return False


    def post(self, request):
        user = request.user
        pair1 = request.data.get('pair1')
        pair2 = request.data.get('pair2')
        time_frame = request.data.get('time_frame')
        timeframe_num = str(request.data.get('timeframe_num'))
        trade = request.data.get('trade')
        slow_move = int(request.data.get('slow_move'))
        fast_move = int(request.data.get('fast_move'))
        position = Position.objects.create(user=user, pair1=pair1, pair2=pair2, time_frame=time_frame, trade=trade,
                                           slow_move=slow_move, fast_move=fast_move, timeframe_num=timeframe_num)
        serializer = PositionSerializer(position, many=False)

        start_at = int((datetime.now() - timedelta(int(slow_move) + 1)).timestamp())
        url_coin = f"https://api.kucoin.com/api/v1/market/candles?type={timeframe_num}{time_frame}&symbol={pair1}-{pair2}&startAt={start_at}"
        response = requests.get(url=url_coin).json()
        data = response['data']
        close_price = []
        for i in range(len(data)):
            close = response['data'][i][2]
            close_price.append(close)

        df = pd.DataFrame(close_price).rolling(slow_move).mean().iloc[-1]

        s = pd.Series(df).item()
        startat1 = int((datetime.now() - timedelta(int(fast_move) + 1)).timestamp())
        url_coin = f"https://api.kucoin.com/api/v1/market/candles?type={timeframe_num}{time_frame}&symbol={pair1}-{pair2}&startAt={startat1}"
        response = requests.get(url=url_coin).json()
        data = response['data']
        close_price = []
        for i in range(len(data)):
            close = response['data'][i][2]
            close_price.append(close)
        df1 = pd.DataFrame(close_price).rolling(fast_move).mean().iloc[-1]

        f = pd.Series(df1).item()

        # threading.Timer(5, self.check_sma(s,f)).start()
        # threading.Thread(target=lambda: every(5, self.check_sma(s,f))).start()
        def print_every_n_seconds(n=2):
            while True:
                print(time.ctime())
                time.sleep(n)

        thread = threading.Thread(target=print_every_n_seconds, daemon=True)
        thread.start()
        while True:
            test = self.check_sma(s, f)
            print(s)
            print(f)
            # timer.run()
            if test:
                print('trooooooo')
                return Response({'data': serializer.data, 'status': True}, status=status.HTTP_200_OK)

            else:
                print('ferooooooo')
                return Response({'data': serializer.data, 'status': False}, status=status.HTTP_200_OK)
