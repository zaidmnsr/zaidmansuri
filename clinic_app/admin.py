from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Clinic)
admin.site.register(Provider)
admin.site.register(Nurse)
admin.site.register(Patient)