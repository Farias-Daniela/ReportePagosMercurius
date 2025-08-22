from django.apps import AppConfig

class UploadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'upload'  # <-- debe coincidir con el nombre de la carpeta

