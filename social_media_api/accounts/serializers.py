from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    following = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all(),
        required=False
    )
    password = serializers.CharField(write_only=True)  # Ensure that this line exists

    class Meta:
        model = User
        fields = ['username', 'email', 'bio', 'profile_picture', 'followers', 'following', 'password']
        read_only_fields = ['followers']

    def create(self, validated_data):
        following = validated_data.pop('following', [])
        user = get_user_model().objects.create_user(**validated_data)  # This line uses get_user_model()

        # Set following relationship if any
        user.following.set(following)
        return user

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Create a new user and return it
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Create a token for the new user
        Token.objects.create(user=user)
        return user


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']
