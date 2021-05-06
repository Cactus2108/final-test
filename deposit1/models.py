from django.db import models

class Deposit(models.Model):
    description = models.FloatField()

    deposit = models.FloatField(max_length=25)
    term = models.IntegerField(max_length=2)
    rate = models.FloatField(max_length=5)
    interest = models.FloatField(max_length=25)

    def __str__(self):
        return f'{self.pk} [{self.description}]'