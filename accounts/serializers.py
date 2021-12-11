from rest_framework import serializers
from rest_framework import exceptions


class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_password(self, value):
        if len(value) < 5:
            raise exceptions.ValidationError('Password is too short')
        elif len(value) > 20:
            raise exceptions.ValidationError('Password is too long')
        return value

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()