import rest_framework.authtoken.views

import django.urls


app_name = 'auth'

urlpatterns = [
    django.urls.path(
        'login/',
        rest_framework.authtoken.views.obtain_auth_token,
        name='login',
    ),
]
