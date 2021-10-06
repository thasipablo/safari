from django.shortcuts import redirect, render

from agence.models import Programme
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