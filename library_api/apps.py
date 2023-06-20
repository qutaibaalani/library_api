from django.apps import AppConfig


# Configuration for the library_api app
class LibraryApiConfig(AppConfig):
    # Set the default auto field for model primary keys
    default_auto_field = "django.db.models.BigAutoField"

    # Set the name of the app
    name = "library_api"
