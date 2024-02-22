import rest_framework_simplejwt.views

import django.urls


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
]
