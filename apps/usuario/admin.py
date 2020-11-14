from django.contrib import admin
from django.contrib.auth.models import User

  
from django_google_maps import fields as map_fields
from django_google_maps import widgets as map_widgets
import json



class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser')
    formfield_overrides = {
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
admin.site.register(User, UserAdmin)

#admin.site.register(User)
