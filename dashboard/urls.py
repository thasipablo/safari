from django.urls import path

from . import views


app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('<id_programme>/details', views.details_programme, name='programme-details'),
]
