from django.db import models

# Create your models here.

class Calc(models.Model):

    a = models.DecimalField(max_digits=12,decimal_places=2)
    b = models.DecimalField(max_digits=12,decimal_places=2)

    def __str__(self):
        return None
