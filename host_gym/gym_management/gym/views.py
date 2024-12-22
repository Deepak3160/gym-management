from rest_framework import viewsets
from .models import User, ClientDetails, TrainerDetails
from .serializers import UserSerializer, ClientDetailsSerializer, TrainerDetailsSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ClientDetailsViewSet(viewsets.ModelViewSet):
    queryset = ClientDetails.objects.all()
    serializer_class = ClientDetailsSerializer

class TrainerDetailsViewSet(viewsets.ModelViewSet):
    queryset = TrainerDetails.objects.all()
    serializer_class = TrainerDetailsSerializer
