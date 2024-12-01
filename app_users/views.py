from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from app_common.pagination import CustomPagination
from .models import UserModel
from .serializers import UserModelSerializer, LoginSerializer


class UserListView(viewsets.ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = UserModel.objects.all()
    # permission_classes = [IsAdminUser]
    pagination_class = CustomPagination

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


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            response = {
                'success': True,
                'message': 'Logout successful'

            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'success': False,
                'message': str(e)
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
