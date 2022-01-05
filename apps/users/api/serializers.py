from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

# custom validators
from .validators import secure_password
from ...utils import get_tokens_for_user

User = get_user_model()


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=40, required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, min_length=8, validators=[secure_password])

    def create(self, validated_data):
        username = validated_data.get('username', None)
        first_name = validated_data.get('first_name', None)
        last_name = validated_data.get('last_name', None)
        email = validated_data.get('email', None)
        password = validated_data.get('password', None)
        user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.save()
        return user

    def validate(self, data):
        username = data.get('username', None)
        email = data.get('email', None)
        if User.objects.filter(username=username).first() :
            raise ValidationError({'message': 'Este usuario no está disponible'})
        elif User.objects.filter(email=email).first():
            raise ValidationError({'message': 'Este correo electrónico no está disponible'})
        return data
