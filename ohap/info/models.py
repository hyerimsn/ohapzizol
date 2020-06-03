from django.db import models

class Beer(models.Model):
    pubname = models.TextField(null=True)
    beername = models.TextField(null=True)
    beerimage = models.ImageField(default = "null")
    # likes = models.ManyToManyField(user, blank=True)
    # 뒤에 settings~~는 user object뒤에 오는 값  settings.AUTH_USER_MODEL
    taste = models.TextField(null=True)
    information = models.TextField(null=True)
    price = models.TextField(null=True)
    alcohol = models.TextField(null=True)

    def __str__(self):
        return self.beername

 

# Create your models here.
