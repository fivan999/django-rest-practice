import django.contrib.admin
import django.contrib.auth.admin

import users.models


class UserAdmin(django.contrib.auth.admin.UserAdmin):
    """отображение модели пользователя в админке"""

    list_display = (
        'pk',
        'username',
        'email',
        'is_active',
        'is_superuser',
    )
    list_display_links = (
        'pk',
        'username',
    )
    list_filter = (
        'is_active',
        'is_superuser',
    )


django.contrib.admin.site.register(users.models.User, UserAdmin)
