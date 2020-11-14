from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect



from django.views.generic import FormView

from apps.googlemaps.forms import SampleForm


class SampleFormView(FormView):
    form_class = SampleForm
    template_name = "googlemaps/index.html"

def index_googlemaps(request):
	return render(request, 'googlemaps/index.html') 
