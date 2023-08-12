from django import forms
from django_select2.cache import cache
from django_select2.forms import (
    HeavySelect2MultipleWidget, HeavySelect2Widget, ModelSelect2TagWidget,
    ModelSelect2Widget, Select2Widget
)
from requests import Request
from .models import *

import select2.fields
import select2.models


class CreatePatientForm(forms.ModelForm):

    # provider = select2.fields.ChoiceField(
    #     choices=Provider.objects.as_choices(),
    #     overlay="Choose an provider...")

    
    class Meta:
        model = Patient
        fields = '__all__' 
        # ['patient_name', 'provider']

    qs = Provider.objects.filter()
    
    provider = forms.ModelChoiceField(
        queryset=Provider.objects.all(),
        # initial={"hello Dolly"},
        label="Provider",
        widget=ModelSelect2Widget(
            attrs={"cols": 80, "rows": 20},
            model=Provider,
            search_fields=['provider_name__icontains'],
        )
    )

    nurse = forms.ModelChoiceField(
        queryset=Nurse.objects.all(),
        label="Nurse",
        widget=ModelSelect2Widget(
            model=Nurse,
            search_fields=['nurse_name__icontains'],
            dependent_fields={'provider': 'works_for_provider'},
            max_results=20,
            
        )
    )





class UpdatePatientForm(forms.ModelForm):

    # provider = select2.fields.ChoiceField(
    #     choices=Provider.objects.as_choices(),
    #     overlay="Choose an provider...")

    
    class Meta:
        model = Patient
        fields = '__all__' 
        # ['patient_name', 'provider']

    qs = Provider.objects.filter()
    
    provider = forms.ModelChoiceField(
        queryset=Provider.objects.all(),
        # initial={"hello Dolly"},
        label="Provider",
        widget=ModelSelect2Widget(
            attrs={"cols": 80, "rows": 20},
            model=Provider,
            search_fields=['provider_name__icontains'],
        )
    )

    nurse = forms.ModelChoiceField(
        queryset=Nurse.objects.all(),
        label="Nurse",
        widget=ModelSelect2Widget(
            model=Nurse,
            search_fields=['nurse_name__icontains'],
            dependent_fields={'provider': 'works_for_provider'},
            max_results=20,
            
        )
    )












# class OLDCreatePatientForm(forms.ModelForm):

    
     
#     # provider = forms.ModelChoiceField(queryset=Provider.objects.all(),
#     #                                  widget=forms.Select(attrs={"hx-get": "load_nurses/", "hx-target": "#id_nurse"}))
#     # looked_by_nurse = forms.ModelChoiceField(queryset=Nurse.objects.none(), to_field_name='looked_by_nurse')


#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)

#     #     if "provider" in self.data:
#     #         id_provider = int(self.data.get("provider"))
#     #         self.fields["looked_by_nurse"].queryset = Nurse.objects.filter(works_for_provider=id_provider)   
          

#     class Meta:
#         model = Patient
#         fields = '__all__'

        
       
    
