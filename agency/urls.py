from django.urls import path

from .apps import AgencyConfig
from . import views


app_name = AgencyConfig.name

urlpatterns = [
    path('programs/', views.programs, name='programs')
]
