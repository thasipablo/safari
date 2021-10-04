from django.urls import path


from . import views

app_name = 'acceuil'

urlpatterns = [
    path('', views.acceuil, name='acceuil')
]
