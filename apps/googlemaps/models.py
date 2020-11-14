from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

from django_google_maps.fields import AddressField, GeoLocationField


class SampleModel(models.Model):
    address = AddressField(max_length=100)
    geolocation = GeoLocationField(blank=True)

    def __str__(self):
        return self.address

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=200)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.nombre


class UbicacionForm(ModelForm):
    class Meta:
        model = Ubicacion
        fields = "__all__" 
