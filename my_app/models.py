from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#table vacation is used to record a vacation
class Vacation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    date_from = models.DateField()
    date_to = models.DateField()

    def __str__(self):
        return  self.description

