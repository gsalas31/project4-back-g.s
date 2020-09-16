from django.contrib.auth import authenticate
from rest_framework import serializers
from apps.authentication.models import User
#from .models import User

#serializer convert data back and forth
class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=255,
        min_length=6,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('fullname', 'email', 'password','token')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)
    toke = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        fields = ('email', 'password', 'token')

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'Email is required to login'
            )
        if password is None:
            raise serializers.ValidationError(
                'Password is required to login'
            )

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'Email or password not found'
            )
        if not user.is_active:
            raise serializers.ValidationError(
                'This is user is no longer active'
            )

        return{
            'email': user.email,
            'toke': user.token
        }
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')