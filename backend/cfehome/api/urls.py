import django.urls
import api.views


urlpatterns = [
    django.urls.path('home/', api.views.home)
]
