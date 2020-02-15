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
