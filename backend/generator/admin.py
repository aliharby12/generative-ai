from django.contrib import admin
from django.apps import apps
from django.utils.module_loading import import_string

app = apps.get_app_config("generator")


class GeneratedTextAdmin(admin.ModelAdmin):
    # Define your custom admin options here
    list_display = ("user", "prompt", "generated_text")
    list_filter = ("user", "prompt")
    search_fields = ("user", "prompt", "generated_text")


class GeneratedImageAdmin(admin.ModelAdmin):
    # Define your custom admin options here
    list_display = ("uuid", "user", "prompt", "image_url")
    list_filter = ("uuid", "user", "prompt")
    search_fields = ("uuid", "user", "prompt", "image_url")


for model in app.get_models():
    model_admin_class_name = f"{model.__name__}Admin"
    try:
        model_admin_class = import_string(f"generator.admin.{model_admin_class_name}")
        admin.site.register(model, model_admin_class)
    except ImportError:
        admin.site.register(model)
