from django.shortcuts import render, redirect

from .models import Programme, Agence
from .forms import ProgrammeForm


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
        return redirect('dashboard:home')

def reservation(request, programme_id):
    return render(request, 'agence/pages/reservation.html')
