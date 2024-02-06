import django.urls

import products.views


app_name = 'products'

urlpatterns = [
    django.urls.path(
        '<int:pk>/',
        view=products.views.ProductDetailAPIView.as_view(),
        name='detail',
    ),
    django.urls.path(
        '',
        view=products.views.ProductListCreateAPIView.as_view(),
        name='list_create',
    ),
]
