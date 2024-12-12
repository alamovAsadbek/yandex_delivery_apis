from rest_framework.viewsets import ModelViewSet
from app_users.models import UserModel
from .serializers import ManagerSerializer, CourierSerializer


class ManagerViewSet(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = ManagerSerializer


class CourierViewSet(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = CourierSerializer
