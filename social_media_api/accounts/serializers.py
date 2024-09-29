from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        following = serializers.PrimaryKeyRelatedField(many=True, queryset=CustomUser.objects.all())
        fields = ['username', 'email', 'bio', 'profile_picture', 'followers']
        read_only_fields = ['followers']

        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Use the user manager to create a new user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
