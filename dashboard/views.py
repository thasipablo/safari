from django.shortcuts import redirect, render
from django.views.generic import FormView

from agence.models import Programme, Reservation
from agence.forms import ProgrammeForm


def dashboard(request):
    context = {
        'programmes': Programme.objects.all().order_by('-id'),
        'form': ProgrammeForm()
    }
    return render(request, 'dashboard/pages/dashboard.html', context)


class NouveauProgramme(FormView):
    form_class = ProgrammeForm
    template_name = 'dashboard/pages/nouveau_programme.html'


def details_programme(request, id_programme):
    programme = Programme.objects.get(id=id_programme)
    if programme:
        reservations = Reservation.objects.filter(programme__id = programme.id).order_by('-id')

        print(reservations)
    else:
        reservations = []

    context = {
        'programmes': Programme.objects.all().order_by('-id'),
        'programme': programme,
        'reservations': reservations,
        'form': ProgrammeForm()
    }
    return render(request, 'dashboard/pages/dashboard.html', context)
