from django.db import models

# Create your models here.
from django.db import models
from core_app.models import BaseModel
from auditlog.registry import auditlog
from django.urls import reverse

# Create your models here.


class Writer(BaseModel):

    writer_name = models.CharField(max_length=150, blank=True,null=True)
    writer_status = models.CharField(max_length=200, blank=True, null=True)
    
    

    

    def get_absolute_url(self):
         return reverse('writer_app:writer_detail', args=[str(self.id)])
    

    def __str__(self):
        return self.writer_name






auditlog.register(Writer)