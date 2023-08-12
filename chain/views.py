from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView
from django.shortcuts import render
from django import forms
from .models import City, State, Country

from django_select2.forms import ModelSelect2Widget
from django.forms import widgets
# Create your views here.

class AddressForm(forms.Form):
    country = forms.ModelChoiceField(
        queryset=Country.objects.all(),

        label="Country",
        widget=ModelSelect2Widget(
            model=Country,
            search_fields=['country__icontains'],
        )
    )
    state = forms.ModelChoiceField(
        queryset=State.objects.all(),
        label="State",
        widget=ModelSelect2Widget(
            model=State,
            search_fields=['state__icontains'],
            dependent_fields={'country': 'country'},
            max_results=500,
        )
    )

    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        label="City",
        widget=ModelSelect2Widget(
            model=City,
            search_fields=['city__icontains'],
            dependent_fields={'state': 'state'},
            max_results=500,
        )
    )






def starten(request):
    form = AddressForm()
    return render(request, 'chain/index.html', {'form': form})
