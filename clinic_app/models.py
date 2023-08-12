from django.db import models
from django.urls import reverse
from django.utils.encoding import force_str

# Create your models here.
class Clinic(models.Model):
    clinic_name = models.CharField(max_length=100, null=True, blank=True)
    clinic_address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.clinic_name


# class ProviderManager(models.Manager):
#     def as_choices(self):
#         for provider in self.all():
#             yield(provider.uid, force_str(provider))

class Provider(models.Model):
    provider_name = models.CharField(max_length=100, null=True, blank=True)
    provider_edu = models.CharField(max_length=100, null=True, blank=True)
    provider_address = models.CharField(max_length=100, null=True, blank=True)
    works_for_clinic = models.ForeignKey(Clinic, on_delete=models.PROTECT, blank=True, null=True)

    # objects = ProviderManager()

    def __str__(self):
        return self.provider_name
    

    

class Nurse(models.Model):
    nurse_name = models.CharField(max_length=100, null=True, blank=True)
    nurse_edu = models.CharField(max_length=100, null=True, blank=True)
    nurse_address = models.CharField(max_length=100, null=True, blank=True)
    works_for_provider = models.ForeignKey(Provider, on_delete=models.PROTECT, blank=True, null=True)
    

    def __str__(self):
        return self.nurse_name
    
class Patient(models.Model):
    patient_name = models.CharField(max_length=100, null=True, blank=True)
    patient_edu = models.CharField(max_length=100, null=True, blank=True)
    patient_address = models.CharField(max_length=100, null=True, blank=True)
    looked_by_nurse = models.ForeignKey(Nurse, on_delete=models.PROTECT, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('clinic_app:create_patient')
    

    def __str__(self):
        return self.patient_name