import products.models

import django.forms
import django.http


def home(request: django.http.HttpRequest) -> django.http.JsonResponse:
    instance = products.models.Product.objects.get(pk=1)
    data = django.forms.model_to_dict(instance)
    return django.http.JsonResponse(data)
