from django.db import models
from core_app.models import BaseModel
from auditlog.registry import auditlog
from django.urls import reverse

# Create your models here.



class TaskTracker(BaseModel):




    task_name = models.CharField(max_length=150, blank=True,null=True)
    task_description = models.TextField(max_length=5000, blank=True,null=True)
    

    class AssignedBy(models.TextChoices):
        LOUISE = 'LOU', 'Louise', 
        FAYEZ = 'FAZ', 'Fayez',
        William = 'WIL', 'William', 
    
    
    class Status(models.TextChoices):
        INPROGRESS = 'INP', 'inProgress', 
        REGULAR = 'REG', 'Regular',
        COMPLETED = 'COM', 'Completed', 
    
    
    class Scope(models.TextChoices):
        NONPROFILE = 'NP', 'Excluded', 
        ADDED = 'REG', 'Added',
        DRIVEN = 'COM', 'Driven', 
     
        



    assigned_by = models.CharField(
        max_length=3,
        choices=AssignedBy.choices,
    default='LOUISE')
    status = models.CharField(
        max_length=3,
        choices=Status.choices,
    default='INPROGRESS')
    scope = models.CharField(
        max_length=3,
        choices=Scope.choices,
    default='WAITING')
        

  

    # def get_absolute_url(self):
    #     return reverse('core_app:core_dashboard', args=[str(self.id)])

    def __str__(self):
        return self.task_name






auditlog.register(TaskTracker)