import django.conf
import django.contrib.admin
import django.urls


urlpatterns = [
    django.urls.path('admin/', django.contrib.admin.site.urls),
    django.urls.path('api/', django.urls.include('api.urls')),
    django.urls.path('api/products/', django.urls.include('products.urls')),
]

if django.conf.settings.DEBUG:
    urlpatterns += (
        django.urls.path(
            '__debug__/', django.urls.include('debug_toolbar.urls')
        ),
    )
