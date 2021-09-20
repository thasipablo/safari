from django.shortcuts import render

from .models import Program, Agency


def programs(request):
    context = {
        'latest_programs': Program.objects.filter().order_by('-id'),
        'agencies': Agency.objects.all()
    }
    return render(request, 'agency/pages/programs.html', context)
