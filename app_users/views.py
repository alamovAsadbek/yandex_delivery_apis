from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserModel
from .serializers import RegisterSerializer, LoginSerializer, DeleteUserSerializer


class RegisterView(APIView):
    serializer_class = RegisterSerializer
    queryset = UserModel.objects.all()

    # permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': True,
            'message': 'User registered successfully.'
        }
        return Response(response, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        users = UserModel.objects.all()
        serializer = self.serializer_class(users, many=True)
        response = {
            'success': True,
            'message': 'List of users',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        user = UserModel.objects.get(id=kwargs['pk'])
        user.delete()
        response = {
            'success': True,
            'message': 'User deleted successfully.'
        }
        return Response(response, status=status.HTTP_200_OK)


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


class DeleteUserView(APIView):
    serializer_class = DeleteUserSerializer
    queryset = UserModel.objects.all()

    def delete(self, request, *args, **kwargs):
        user = UserModel.objects.get(id=kwargs['pk'])
        user.delete()
        response = {
            'success': True
        }
        return Response(response, status=status.HTTP_200_OK)
