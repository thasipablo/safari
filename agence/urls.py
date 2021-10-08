from django.urls import path

from . import views


app_name = 'agence'

urlpatterns = [
    path('programmes/', views.programmes, name='programmes'),
    path('enregistrer-programme/', views.enregistrer_programme, name='enregister-programme'),
    path('programmes/<programme_id>/reservation/', views.reservation, name='reservation')
]
