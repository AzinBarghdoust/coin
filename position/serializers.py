from rest_framework import serializers
from .models import Position


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

    def validate(self, attrs):
        if attrs['slow_move'] == attrs['fast_move']:
            raise serializers.ValidationError('these 2 value should not be the same!')
        return attrs



