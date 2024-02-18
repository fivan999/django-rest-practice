import algoliasearch_django
import algoliasearch_django.decorators

import products.models


@algoliasearch_django.decorators.register(products.models.Product)
class ProductModelIndex(algoliasearch_django.AlgoliaIndex):
    """индекс Algolia для модели Product"""

    fields = ('title', 'description', 'user')
    index_name = 'product_index'
