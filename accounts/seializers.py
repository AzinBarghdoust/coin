from rest_framework import serializers, validators
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.translation import gettext_lazy as _


class UserLoginSerializer(TokenObtainPairSerializer):
    """Customizes JWT default Serializer to add more information about user"""

    @classmethod
    def get_token(cls, user):
        token = super(UserLoginSerializer, cls).get_token(user)
        token['email'] = user.email
        token['password'] = user.password

        return token


class UserRegisterSerializer(serializers.ModelSerializer):
    password_conf = serializers.CharField(max_length=128, required=True, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True},
            "email": {
                "required": True,
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(),
                        message="This email has already taken!",
                    )
                ]
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            password2=validated_data['password2']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    def validate_username(self, value):
        if value != 'email':
            raise serializers.ValidationError('Change username')
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('password is not match!')
        return data
