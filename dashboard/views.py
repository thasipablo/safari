from django.shortcuts import redirect, render

from agence.models import Programme, Reservation
from agence.forms import ProgrammeForm


def dashboard(request):
    context = {
        'programmes': Programme.objects.all(),
        'form': ProgrammeForm()
    }
    return render(request, 'dashboard/pages/dashboard.html', context)


def nouveau_programme(request):
    if request.method == 'POST':
        form = ProgrammeForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('dashboard:home')


def details_programme(request, id_programme):
    programme = Programme.objects.get(id=id_programme)
    if programme:
        reservations = Reservation.objects.filter(programme__id = programme.id)

        print(reservations)
    else:
        reservations = []

    context = {
        'programmes': Programme.objects.all(),
        'programme': programme,
        'reservations': reservations,
        'form': ProgrammeForm()
    }
    return render(request, 'dashboard/pages/dashboard.html', context)
