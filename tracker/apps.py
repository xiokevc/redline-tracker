from django.apps import AppConfig


class TrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tracker'
    verbose_name = 'Vehicle Maintenance Tracker'

    def ready(self):
        pass
