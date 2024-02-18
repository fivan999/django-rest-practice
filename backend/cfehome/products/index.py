import algoliasearch_django
import algoliasearch_django.decorators

import products.models


@algoliasearch_django.decorators.register(products.models.Product)
class ProductModelIndex(algoliasearch_django.AlgoliaIndex):
    """индекс Algolia для модели Product"""

    fields = ('title', 'description', 'user', 'is_public')
    settings = {
        'attributesForFaceting': ['user', 'is_public'],
        'searchableAttributes': ['title', 'description'],
    }
    index_name = 'product_index'
