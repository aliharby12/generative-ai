from django.contrib import admin
from django.apps import apps, AppConfig
from django.utils.module_loading import import_string
from typing import Type

app: AppConfig = apps.get_app_config("generator")


class GeneratedTextAdmin(admin.ModelAdmin):
    # Define your custom admin options here
    list_display: tuple[str, str, str] = ("user", "prompt", "generated_text")
    list_filter: tuple[str, str] = ("user", "prompt")
    search_fields: tuple[str, str, str] = ("user", "prompt", "generated_text")


class GeneratedImageAdmin(admin.ModelAdmin):
    # Define your custom admin options here
    list_display: tuple[str, str, str, str] = ("uuid", "user", "prompt", "image_url")
    list_filter: tuple[str, str, str] = ("uuid", "user", "prompt")
    search_fields: tuple[str, str, str, str] = ("uuid", "user", "prompt", "image_url")


for model in app.get_models():
    model_admin_class_name: str = f"{model.__name__}Admin"
    try:
        model_admin_class: Type[admin.ModelAdmin] = import_string(
            f"generator.admin.{model_admin_class_name}"
        )
        admin.site.register(model, model_admin_class)
    except ImportError:
        admin.site.register(model)
