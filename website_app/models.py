from django.db import models
from core_app.models import BaseModel
from django.urls import reverse
from auditlog.registry import auditlog


#
    
# Create your models here.
class AmazonAssociates(models.Model):

    AMAZONUSA = "USA"
    AMAZONINDIA = "IND"

    AMAZON_LOCATION_CHOICES = [
        (AMAZONUSA, "Amazon USA"),
        (AMAZONINDIA, "Amazon India"),
        
    ]
    
    amazon_associates_email = models.EmailField(max_length=100, null=True)
    amazon_tag = models.CharField(max_length=150, null=True)
    amazon_location = models.CharField(
        max_length=5,
        choices=AMAZON_LOCATION_CHOICES,
        default=AMAZONUSA,
    )


class DomainProviders(models.Model):
    provider_name = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.provider_name
    
class HostingProviders(models.Model):
    provider_name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.provider_name

    

class Website(BaseModel):

    FREQUENCY_PUBLISHING = (
        ('OnceDaily', 'OnceDaily'),
        ('4/Week', '4/Week'),
    )
    website_name = models.CharField(max_length=50, null=True, blank=True)
    website_url = models.URLField(max_length=100, null=True, blank=True)
    admin_website = models.CharField(max_length=100, null=True, blank=True)
    admin_pass = models.CharField(max_length=100, null=True, blank=True)
    user_website = models.CharField(max_length=100, null=True, blank=True)
    user_pass = models.CharField(max_length=100, null=True, blank=True)
    email_website = models.EmailField(max_length=100, null=True, blank=True)
    email_pass = models.CharField(max_length=100, null=True, blank=True)
    amazon_email = models.ForeignKey(AmazonAssociates, on_delete=models.PROTECT, null=True, blank=True, related_name="associate_email")
    amazon_associates_tag = models.OneToOneField(AmazonAssociates, on_delete=models.PROTECT, null=True, blank=True, related_name="associate_tag")
   
    server =  models.URLField(max_length=100, null=True, blank=True)
    domain_provider = models.ForeignKey(DomainProviders, null=True, blank=True, on_delete=models.PROTECT) 
    hosting_provider = models.ForeignKey(HostingProviders, null=True, blank=True, on_delete=models.PROTECT) 
    publishing_frequency = models.CharField(max_length=20, choices=FREQUENCY_PUBLISHING, default='OnceDaily')
   
    def get_absolute_url(self):
        return reverse('website_app:website_detail', args=[str(self.id)])

    def __str__(self):
        return self.website_name







auditlog.register(Website)



