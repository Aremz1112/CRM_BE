from django.apps import AppConfig
from mongoengine import connect


class CrmBackendAppV1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CRM_BackEnd_app_v1'
    def ready(self) :
            connect(db="db",
            host="mongodb+srv://Aremu:Aremz1112@db.lktsvzf.mongodb.net/?appName=db",)
            