import typing

import algoliasearch.search_index
import algoliasearch_django


def extract_search_params(
    request_get: dict, available_params: dict[str, typing.Callable]
) -> dict:
    """получаем параметры поиска из словаря request.GET"""
    params = {}
    for param in available_params:
        val = request_get.get(param, '')
        if val:
            params[param] = available_params[param](val)
    return params


def get_search_index(
    index_name: str,
) -> algoliasearch.search_index.SearchIndex:
    """возвращаем объект индекса по его названию"""
    return algoliasearch_django.algolia_engine.client.init_index(index_name)


def get_search_results(query: str, search_index: str, **kwargs) -> dict:
    """
    получаем ответ от algolia в виде словаря
    по запросу query и search_index
    """
    search_params = {}
    kwargs_filters = [f'{k}:{v}' for k, v in kwargs.items() if v]
    if kwargs_filters:
        search_params['facetFilters'] = kwargs_filters
    index = get_search_index(search_index)
    return index.search(query, search_params)


def get_results_ids(query: str, search_index: str, **kwargs) -> list[int]:
    """получаем id записей по запросу query и search_index"""
    result_inds = [
        int(item['objectID'])
        for item in get_search_results(query, search_index, **kwargs)['hits']
    ]
    return result_inds
