import rest_framework.routers

import products.views
import products.viewsets


app_name = 'products'

router = rest_framework.routers.SimpleRouter()
router.register('products', products.viewsets.ProductViewSet)

urlpatterns = router.urls
