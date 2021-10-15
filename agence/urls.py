from django.urls import path

from . import views


app_name = 'agence'

urlpatterns = [
    path('reservation/pay/', views.paypal, name="pay-reservation"),
    path('reservation/succes/<code>', views.reservation_succes, name="reservation_succes"),
    path('programmes/', views.programmes, name='programmes'),
    path('enregistrer-programme/', views.enregistrer_programme, name='enregister-programme'),
    path('enregistrer-reservation/', views.enregistrer_reservation, name='enregistrer_reservation'),
    path('programmes/<programme_id>/reservation/', views.reservation, name='reservation')
]
