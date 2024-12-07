from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from app_common.pagination import CustomPagination
from app_products import models as products_models
from app_products import serializers as products_serializers
from .models import UserModel
from .serializers import UserModelSerializer, LoginSerializer


class UserListView(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited. This api for super admin only.
    """
    serializer_class = UserModelSerializer
    queryset = UserModel.objects.all()
    # permission_classes = [IsAdminUser]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save()


class LoginView(APIView):
    """
        API endpoint that allows users to login.
    """
    serializer_class = LoginSerializer
    queryset = UserModel.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        refresh = RefreshToken.for_user(serializer.validated_data['user'])
        response = {
            'success': True,
            'message': 'Login successful',
            'token': {
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            }
        }
        return Response(response, status=status.HTTP_200_OK)


class LogoutView(APIView):
    """
        API endpoint that allows users to logout.
    """

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


class GetAllProductsView(APIView):
    serializer_class = products_serializers.ProductSerializer
    queryset = products_models.ProductsModel.objects.all()

    def get(self, request, *args, **kwargs):
        products = products_models.ProductsModel.objects.all()
        serializer = products_serializers.ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
