from django.urls import path

from app_users import views as user_views

urlpatterns = [
    # auth urls
    path('auth/register/', user_views.RegisterView.as_view(), name='register'),
    path('auth/login/', user_views.LoginView.as_view(), name='login'),
    path('auth/logout/', user_views.LogoutView.as_view(), name='logout'),

    # user urls
    path('users/', user_views.UserListView.as_view(), name='user-list'),
]
