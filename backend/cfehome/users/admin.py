import users.models

import django.contrib.admin
import django.contrib.auth.admin


class UserAdmin(django.contrib.auth.admin.UserAdmin):
    """отображение модели пользователя в админке"""

    ...


django.contrib.admin.site.register(users.models.User, UserAdmin)
