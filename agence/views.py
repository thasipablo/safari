from django.shortcuts import render, redirect

from .models import Programme, Agence


def programmes(request):
    context = {
        'dernier_programmes': Programme.objects.filter().order_by('-id'),
        'agences': Agence.objects.all()
    }
    return render(request, 'agence/pages/programmes.html', context)


def reservation(request, programme_id):
    return render(request, 'agence/pages/reservation.html')
