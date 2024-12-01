from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserModel
from .serializers import RegisterSerializer, LoginSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = UserModel.objects.all()

    # permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()


class LoginView(APIView):
    serializer_class = LoginSerializer
    queryset = UserModel.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success': True
        }
        return Response(response, status=status.HTTP_200_OK)
