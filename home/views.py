from django.shortcuts import render

from agency.models import Program, Agency


def home(request):
    context = {
        'latest_programs': Program.objects.filter().order_by('-id'),
        'agencies': Agency.objects.all()
    }
    return render(request, 'home/home.html', context)
