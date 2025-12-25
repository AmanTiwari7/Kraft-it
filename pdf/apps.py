from django.apps import AppConfig


class PdfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pdf'
    verbose_name = 'PDF Operations'
    
    def ready(self):
        """
        Called when Django starts.
        Good place to register signals, etc.
        """
        pass