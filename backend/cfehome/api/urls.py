import api.views

import django.urls


app_name = 'api'

urlpatterns = [
    django.urls.path('home/', api.views.home, name='home'),
]
