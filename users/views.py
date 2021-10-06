from django.shortcuts import redirect

from  .utils import hasGroup

def register(request):
    pass


def redirection(request):
    user = request.user
    if hasGroup(user, 'administrator'):
        return redirect('dashboard:home')
    
    else:
        return redirect('dashboard:supervisor')