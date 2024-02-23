import rest_framework_simplejwt.views

import django.urls

import users.viewsets


app_name = 'auth'

urlpatterns = [
    django.urls.path(
        'token/',
        rest_framework_simplejwt.views.TokenObtainPairView.as_view(),
        name='token_obtain',
    ),
    django.urls.path(
        'token/refresh/',
        rest_framework_simplejwt.views.TokenRefreshView.as_view(),
        name='token_refresh',
    ),
    django.urls.path(
        'token/verify/',
        rest_framework_simplejwt.views.TokenVerifyView.as_view(),
        name='token_verify',
    ),
    django.urls.path(
        'users/',
        users.viewsets.UserViewSet.as_view({'post': 'create'}),
        name='create_user',
    ),
    django.urls.path(
        'users/activate/<uidb64>/<token>/',
        users.viewsets.UserViewSet.as_view({'get': 'activate_user'}),
        name='activate_user',
    ),
    django.urls.path(
        'users/<int:pk>/change-password/',
        users.viewsets.UserViewSet.as_view(
            {'put': 'change_password', 'patch': 'change_password'}
        ),
        name='change_password',
    ),
]
