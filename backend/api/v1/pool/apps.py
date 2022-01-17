from django.apps import AppConfig


class PoolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.v1.pool'
    verbose_name = 'Платформа для опросов'
