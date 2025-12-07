from django.apps import AppConfig #определяет поведение и настройки конкретного приложения


class CatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'
