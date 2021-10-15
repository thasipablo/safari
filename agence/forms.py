from django.forms import ModelForm
from .models import Programme, Reservation, Client


class ProgrammeForm(ModelForm):
    class Meta:
        model = Programme
        fields = ['prix', 'itineraire', 'date_depart', 'heure_depart', 'places']

        
class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

        
class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'telephone', 'email', 'places']


