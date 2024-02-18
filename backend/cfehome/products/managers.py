import typing

import django.db.models


class ProductManager(django.db.models.Manager):
    """менеджер модели Product"""

    def search_by_user(
        self, user_pk: typing.Optional[int] = None
    ) -> django.db.models.QuerySet:
        """поискт товаров по пользователю"""
        return self.filter(
            django.db.models.Q(is_public=True)
            | django.db.models.Q(user__pk=user_pk)
        )
