from .models import Agence, Programme, Client, Itineraire, Reservation
from django.contrib import admin


@admin.register(Agence)
class AgenceAdmin(admin.ModelAdmin):
    model = Agence
    list_display = ('denomination', 'localisation', 'telephone')


@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    model = Programme
    list_display = ('itineraire', 'date_depart', 'heure_depart', 'prix')

    
@admin.register(Itineraire)
class ItineraireAdmin(admin.ModelAdmin):
    model = Itineraire
    list_display = ('lieu_depart', 'lieu_arrive')

    
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    list_display = ('programme', 'client')

    
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ('nom', 'telephone', 'email')
