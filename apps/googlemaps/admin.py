from django.db import models
from django_google_maps import fields as map_fields
from django_google_maps import widgets as map_widgets

from django.contrib import admin
from django.contrib.auth.models import User
import json
from apps.googlemaps.models import Ubicacion, SampleModel
from django.contrib import admin
from django.forms.widgets import TextInput

from django_google_maps.widgets import GoogleMapsAddressWidget
from django_google_maps.fields import AddressField, GeoLocationField



class SampleModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        AddressField: {
            'widget': GoogleMapsAddressWidget
        },
        GeoLocationField: {
            'widget': TextInput(attrs={
                'readonly': 'readonly'
            })
        },
    }

admin.site.register(Ubicacion)
admin.site.register(SampleModel, SampleModelAdmin)


""" class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
          'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    }
 """
""" class RentalAdmin(admin.ModelAdmin): formfield_overrides = {
    map_fields.AddressField: { 'widget':
    map_widgets.GoogleMapsAddressWidget(attrs={
      'data-autocomplete-options': json.dumps({ 'types': ['geocode',
      'establishment'], 'componentRestrictions': {
                  'country': 'us'
              }
          })
      })
    },
}




admin.site.unregister(User) 
admin.site.register(User, RentalAdmin) """
