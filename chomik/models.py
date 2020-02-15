from django.contrib.postgres.fields import JSONField
from django.db import models

class Sala(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    projector = models.BooleanField()

    def is_unavailable(self, date):
        return self.reserwacje.filter(date=date).exists()


class Reserwacja(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='rezerwacje')
    date = models.DateField()
    comment = models.TextField()



class SprzetKomputerowy(models.Model):
    producent = models.CharField(max_length=64)
    waga = models.PositiveIntegerField() # W gramach
    sn = models.CharField(max_length=64, null=True)
    class Meta:
        abstract=True

class Pecet(SprzetKomputerowy):
    zasilacz = models.CharField(max_length=64)
    karta_graficzna = models.CharField(max_length=64)

class Laptop(SprzetKomputerowy):
    ekran = models.CharField(max_length=64)
    usb_count = models.CharField(max_length=64)


class ChomikDżejson(models.Model):
    json = JSONField()
