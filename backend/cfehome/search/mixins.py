import abc
import typing

import django.db.models

import search.services


class ListSearchMixin:
    """миксин для посика по списку"""

    availabe_search_params = dict[str, typing.Callable]
    index_name: str

    @abc.abstractmethod
    def get_default_queryset(self) -> django.db.models.QuerySet:
        """базовый queryset для поиска"""
        ...

    def get_queryset(self) -> django.db.models.QuerySet:
        """
        получаем queryset в зависимости от поискового запроса
        """
        if self.action == 'list':
            default_queryset = self.get_default_queryset()

            query = self.request.GET.get('query', '')

            params = search.services.extract_search_params(
                self.request.GET, self.availabe_search_params
            )

            if not params and not query:
                return default_queryset

            return default_queryset.filter(
                pk__in=search.services.get_results_ids(
                    query, self.index_name, **params
                )
            )
        return self.__class__.queryset
