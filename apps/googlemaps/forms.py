from django import forms
from apps.googlemaps.models import Ubicacion, SampleModel
from django_google_maps.widgets import GoogleMapsAddressWidget


class SampleForm(forms.ModelForm):

    class Meta(object):
        model = SampleModel
        fields = ['address', 'geolocation']
        widgets = {
            "address": GoogleMapsAddressWidget,
        }