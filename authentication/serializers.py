from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import exceptions


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username', 'password',)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    """
    Authenticates user.
    """

    username = serializers.CharField(max_length=255, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        """
        Validates user data.
        """
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError(
                'A username is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=username, password=password)

        if user is None:
            raise exceptions.AuthenticationFailed(
                'A user with this username and password was not found.')
        else:
            token, _ = Token.objects.get_or_create(user=user)
            user.token = token.key

        if not user.is_active:
            raise exceptions.NotFound('This user has been deactivated.')

        return {
            'token': user.token
        }


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Registration user.
    """

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password',)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.token = Token.objects.create(user=user).key

        return user
