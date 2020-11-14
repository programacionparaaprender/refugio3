from django.contrib import admin
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.contrib import admin
from django.urls import path, reverse_lazy
from django.conf.urls import url, include
from django.contrib.auth import login
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

dic_1 =  {
'template_name':'registration/password_reset_form.html',
'email_template_name': 'registration/password_reset_email.html'
}
dic_2 =  {
'template_name': 'registration/password_reset_done.html'
}
dic_3 =  {
'template_name': 'registration/password_reset_confirm.html'
}
dic_4 = {
'template_name': 'registration/password_reset_complete.html'
}

from .views import redirect_view

urlpatterns = [
    path('', redirect_view),
    path('admin/', admin.site.urls),
    path('googlemaps/', include('apps.googlemaps.urls')),
    path('mascota/', include('apps.mascota.urls')),
    path('adopcion/', include('apps.adopcion.urls')),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^usuario/', include('apps.usuario.urls')),
    url(r'^accounts/login/', LoginView.as_view(template_name='index.html'), name='login'),
    path('reset/password_reset', PasswordResetView.as_view(), dic_1, name='password_reset'), 
    path('password_reset_done', PasswordResetDoneView.as_view(), dic_2, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), dic_3,name='password_reset_confirm'),
    path('reset/done', PasswordResetCompleteView.as_view(), dic_4,name='password_reset_complete'), 
]

