from django.db import models

# Create your models here.


class Country(models.Model):
    country = models.CharField(max_length=20)
    
    def __str__(self):
        return self.country
    

class State(models.Model):
    state = models.CharField(max_length=20)
    country = models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.state
    

class City(models.Model):
    city = models.CharField(max_length=20)
    state = models.ForeignKey(State,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.city
    