from django.db import models

class Beer(models.Model):
    pubname = models.TextField(null=True)
    beername = models.TextField(null=True)
    beerimage = models.ImageField(default = "null")

    taste = models.TextField(null=True)
    information = models.TextField(null=True)
    price = models.TextField(null=True)
    alcohol = models.TextField(null=True)

    def __str__(self):
        return self.beername

# Create your models here.
