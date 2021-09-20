from django.db import models


class Agency(models.Model):
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Itinerary(models.Model):
    pass


class Program(models.Model):
    # itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    go_from = models.CharField(max_length=250)
    go_to = models.CharField(max_length=250)
    agency = models.ForeignKey(
        Agency, related_name="programs", on_delete=models.CASCADE)
    go_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    places = models.IntegerField()

    def __str__(self):
        return f'{self.go_from} to {self.go_to} - {self.agency.name}'
