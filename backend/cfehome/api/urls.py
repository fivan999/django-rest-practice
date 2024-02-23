import django.urls


urlpatterns = [
    django.urls.path('', django.urls.include('products.urls')),
    django.urls.re_path('auth/', django.urls.include('users.urls')),
]
