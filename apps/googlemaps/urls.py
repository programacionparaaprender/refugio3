from apps.usuario.views import SampleFormView
from  django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('', login_required(SampleFormView.as_view()), name="googlemaps"),
]