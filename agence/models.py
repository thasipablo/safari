from django.db import models


class Agence(models.Model):
    denomination = models.CharField(max_length=250)
    localisation = models.CharField(max_length=250)
    detail_infos = models.TextField(blank=True, null=True)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, null=True, blank=True)
    proprietaire = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return f'{self.denomination}'


class Itineraire(models.Model):
    lieu_depart = models.CharField(max_length=250)
    lieu_arrive = models.CharField(max_length=250)
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.lieu_depart} - {self.lieu_arrive}'

class Programme(models.Model):
    # itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    prix = models.FloatField()
    itineraire = models.ForeignKey(
        Itineraire, related_name="itineraires", on_delete=models.CASCADE)
    date_depart = models.DateField()
    heure_depart = models.TimeField()
    places = models.IntegerField()
    places_libres = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.itineraire} - {self.prix}'

      
class Reservation(models.Model):
    code = models.CharField(max_length=50, default='')
    programme =  models.ForeignKey(Programme, on_delete=models.CASCADE)
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    paye = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.programme} - {self.client}'


class Client(models.Model):
    nom = models.CharField(max_length=250, verbose_name='Nom Complet')
    telephone = models.CharField(max_length=250, verbose_name="Numero de Telephone")
    email = models.EmailField(max_length=254, null=True, blank=True)
    places = models.IntegerField(default=1)
    programme =  models.ForeignKey(Programme, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.nom} - {self.telephone}'