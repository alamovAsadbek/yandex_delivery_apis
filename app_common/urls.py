from django.urls import path

from app_users import views as user_views

urlpatterns = [
    path('auth/', user_views.RegisterView.as_view(), name='register'),
]
