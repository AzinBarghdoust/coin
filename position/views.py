from django.contrib.sites import requests
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from position.serializers import *
import requests


class Position(APIView):
    pass


class CreatePosition(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        pair1 = request.data['pair1']
        pair2 = request.data['pair2']
        time_frame = request.data['time_frame']
        trade = request.data['trade']
        slow_move = request.data['slow_move']
        fast_move = request.data['fast_move']
        # operator = request.data['operator']

        position = Position.objects.create(pair1=pair1, pair2=pair2, time_frame=time_frame, trade=trade,
                                           slow_move=slow_move, fast_move=fast_move)
        serializer = PositionSerializer(position, many=False)

        return Response({'data': serializer.data})


