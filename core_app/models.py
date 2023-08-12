from django.db import models
from auditlog.registry import auditlog
import uuid


# Create your models here.


class BaseModel(models.Model):

    PUBLISHING_STATUS_CHOICES = (
        ('Live', 'Live'),    
        ('Publishing', 'Publishing'),    
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    publishing_status = models.CharField(max_length=20,choices=PUBLISHING_STATUS_CHOICES, default='Live')
    is_active = models.BooleanField(default=True)
   

    date_created = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)




    class Meta:
        abstract = True


auditlog.register(BaseModel)