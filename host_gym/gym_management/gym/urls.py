from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ClientDetailsViewSet, TrainerDetailsViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'clients', ClientDetailsViewSet)
router.register(r'trainers', TrainerDetailsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
