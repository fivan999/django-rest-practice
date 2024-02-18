import algoliasearch.search_index
import algoliasearch_django


def get_search_index(
    index_name: str,
) -> algoliasearch.search_index.SearchIndex:
    """возвращаем объект индекса по его названию"""
    return algoliasearch_django.algolia_engine.client.init_index(index_name)


def perform_search(query: str, search_index: str) -> list[int]:
    """поиск id моделей по запросу query и search_index"""
    index = get_search_index(search_index)
    result_inds = [
        int(item['objectID']) for item in index.search(query)['hits']
    ]
    return result_inds
