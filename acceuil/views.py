from django.shortcuts import render

from agence.models import Programme, Agence


def acceuil(request):
    context = {
        'dernier_programmes': Programme.objects.filter().order_by('-id'),
        'agences': Agence.objects.all(),
        'home': True,
    }
    return render(request, 'acceuil/acceuil.html', context)
