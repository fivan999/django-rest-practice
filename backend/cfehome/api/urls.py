import django.urls

import api.views


app_name = 'api'

urlpatterns = [
    django.urls.path('home/', api.views.home, name='home'),
]
