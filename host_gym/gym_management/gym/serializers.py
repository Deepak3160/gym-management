from rest_framework import serializers
from .models import User, ClientDetails, TrainerDetails

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ClientDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientDetails
        fields = '__all__'

class TrainerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainerDetails
        fields = '__all__'
