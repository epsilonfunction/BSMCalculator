
from django.db import models

class BSMCalculation(models.Model):
    
    created = models.DateTimeField(auto_now_add=True)
    
    S = models.FloatField()
    K = models.FloatField()
    r = models.FloatField()
    t = models.FloatField()
    q = models.FloatField()
    sigma = models.FloatField()
    
    # call = models.FloatField()
    # put = models.FloatField()


class SampleItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    
    def __str__(self):
        return self.name
