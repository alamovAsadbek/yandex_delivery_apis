from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import UserModel
from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = UserModel.objects.all()
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()
