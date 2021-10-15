from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Client, Programme, Agence, Reservation
from .forms import ProgrammeForm, ReservationForm, ClientForm


def programmes(request):
    context = {
        'dernier_programmes': Programme.objects.filter().order_by('-id'),
        'agences': Agence.objects.all()
    }
    return render(request, 'agence/pages/programmes.html', context)


def paypal(request):
    return render(request, 'agence/pages/paypal.html')


def enregistrer_programme(request):
    if request.method == "POST":
        form = ProgrammeForm(request.POST)
        if form.is_valid():
            form.save()
        
        prog = Programme.objects.latest('id')
        prog.places_libres = request.POST["places"]
        prog.save()
        return redirect('dashboard:home')


def reservation(request, programme_id):
    form = ClientForm()
    return render(request, 'agence/pages/reservation.html', {'form': form, 'programme': programme_id})


def enregistrer_reservation(request):
    if request.method == 'POST':
        print('programme:', request.POST['programme'])
        form = ClientForm(request.POST)
        if (form.is_valid):
            form.save()
        
        programme = Programme.objects.get(id=request.POST['programme'])
        client = Client.objects.latest('id')

        code = f"{request.POST['nom'][0]}-{request.POST['telephone'][3:5]}-{request.POST['programme']}"
        reservation = Reservation(programme=programme, client=client, code=code)
        reservation.save()
        
        # mettre à jour les places
        programme.places_libres -= client.places
        programme.save()
        
        return redirect(reverse('agence:reservation_succes', kwargs=code))


def reservation_succes(request, code):
    return render(request, 'agence/pages/reservation-succes.html', {'code': code})