from django.db import models

# Create your models here.
class Bmi(models.Model):
    height = models.FloatField()
    weight = models.FloatField()
    
    def bmi(self):
        return self.weight / self.height ** 2

class Wth(models.Model):
    waist = models.FloatField()
    hip = models.FloatField()
    
    def wth(self):
        return self.waist / self.hip

