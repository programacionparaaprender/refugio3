pendiente
https://pypi.org/project/django-faker/
https://simpleisbetterthancomplex.com/tutorial/2016/08/29/how-to-work-with-ajax-request-with-django.html

multiselect django
https://github.com/madisona/django-multiselect


google maps
https://pypi.org/project/django-google-maps/
python -m pip install django-google-maps

pendiente cifrado de contraseña
https://stackoverflow.com/questions/9571624/how-do-i-get-the-password-in-django


pendiente Vue
https://pypi.org/project/python_vuejs/
https://github.com/taogeT/flask-vue/tree/master/flask_vue/static

----------------------------
0.
----------------------------
Curso
https://www.youtube.com/watch?v=yDnZ0hJBDmc&list=PLsRdPvQ2xMkH8c2BOnQ_O1KZ9lyyL_eGB&index=25
https://pypi.org/project/django-bootstrap4/
https://blog.nubecolectiva.com/como-integrar-django-y-bootstrap-4/
https://realpython.com/django-redirects/#:~:text=Django%20Redirects%3A%20A%20Super%20Simple%20Example,-In%20Django%2C%20you&text=Just%20call%20redirect()%20with,then%20return%20from%20your%20view.&text=Assuming%20this%20is%20the%20main,to%20%2Fredirect%2Dsuccess%2F%20.
https://docs.djangoproject.com/en/3.1/topics/class-based-views/intro/
https://www.django-rest-framework.org/api-guide/status-codes/

python -m pip install virtualenv
python -m venv django_venv3

python -m pip install django

python -m pip install pymysql
python -m pip install mysqlclient
python -m pip list

python -m pip install bootstrap4
python -m pip install djangorestframework
python -m pip install django-bootstrap4


--------------
1. Creando proyecto y app
------------------------
settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'refugio',
        'USER': 'root',
        'PASSWORD': '',
    }
}

django-admin.py startproject refugio

python manage.py migrate

python manage.py createsuperuser
yancel209@gmail.com
admin
12345678

python manage.py runserver

-----------------------------------
Iteraci�n 3: Crear proyecto
-----------------------------------
mkdir apps
cd apps 
django-admin.py startapp mascota
django-admin.py startapp adopcion
django-admin.py startapp usuario



-----------------------
----------------------
4. crear aplicaciones estructura del proyecto
-------------------
---------------------

django-admin.py startproject refugio
cd refugito
mkdir apps
cd apps
django-admin.py startapp mascota
django-admin.py startapp adopcion

python manage.py migrate

----------------------------
5. Modelos y migraciones
-----------------------------
models.py mascotas
models.py adopcion

python manage.py makemigrations
python manage.py migrate

-----------------------------
6.- Curso Django - Relaciones
------------------------
admin.py mascotas
admin.py adopcion
python manage.py migrate

-------------------------
7.- Curso Django - Django Shell y Querysets
--------------------------------------
python manage.py shell
from apps.adopcion.models import Persona
from apps.mascota.models import Vacuna,Mascota

Persona.objects.create(nombre="Luis",apellido="Correa",edad=26,telefono="3434123",email="alberto13711@gmail.com",domicilio="Venezuela")
#si se usan variables hay que hacerlo as�
p = Persona.objects.create(nombre="Percy",apellido="Correa",edad=67,telefono="3434123",email="percyelias20@outlook.com",domicilio="Venezuela")
p.save()

v1 = Vacuna(nombre="vacuna 3")
v1.save()
v2 = Vacuna(nombre="vacuna 2")
v2.save()
v3 = Vacuna(nombre="vacuna 1")
v3.save()
mascota1 = Mascota.objects.create(nombre="Pepe",sexo="macho",edad_aproximada=1,fecha_rescate="2016-09-01",persona=p)
mascota1.save()
mascota1.vacuna.add(v1)

Mascota.objects.all()
Mascota.objects.filter(id=1)
Mascota.objects.filter(nombre__contains="1")


--------------------------------------------------
8.- Curso Django - Configurar URLs y primera view
---------------------------------------------------
mascota/views.py
mascota/urls.py
mascota/forms.py

adopcion/views.py
adopcion/urls.py
adopcion/forms.py

refugio/urls.py

python manage.py runserver 8080


-------------------------------------
9. Curso Django - Sistema Plantillas
-------------------------------------
settings.py se coloca la ubicación

------------------------------
10. Curso Django - Herencia de plantillas
----------------------------------------
templates/base/base.html

-------------------
11.- Curso Django - Configurar archivos estáticos
---------------------------------------------
colocar ubicaciones del los static en el settings.py
y en los otros archivos


--------------------------------
12.- Curso Django - Formularios y vistas basadas en funciones crear
----------------------------------------
forms.py de mascotas
views.py de mascotas

--------------------------------
17.- Curso Django - CRUD con dos formularios Parte 1
----------------------------------------
se validan los datos de dos formularios
adopcion/views.py
SolicitudCreate

--------------------------
19.- Curso Django - Crear Registro de Usuarios (modelo)
---------------------------------

django-admin.py startapp usuario

----------------------
-----------------------
20.- Curso Django - Crear login (facilito)
----------------------------


----------------------------
21.- Curso Django - Recuperar contraseña por correo (facilito)
--------------------------------------------------------------
https://stackoverflow.com/questions/52502862/django-2-1-passwordresetview-404
https://stackoverflow.com/questions/49434711/trying-to-customize-the-django-setpasswordform
https://docs.djangoproject.com/en/2.0/topics/auth/default/#module-django.contrib.auth.views
https://www.youtube.com/watch?v=qjlZWBbX7-o
nueva contraseña
admin
3YDZjZG3MWYwg

habilitar acceso a aplicaciones poco seguras
https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4NdnwllzKEFoXU8bkr-kzcJOR87ulJtfWipyNbK2cvH-SkG7T8Esj0LAU9bDCoQ4faWtHrbei41gmtk1ZiqbLD6WD6frQ

--------------------------
22.- Curso Django - Decorador login required
---------------------------------------------
login_required

---------------------
23.- Curso Django - Serializar objetos
----------------------------
Crear una api rest

----------------------
24.- Curso Django - Paginación
-----------------
mascota_list.html
<ul class="pager">
	<li style="display: inline;background-color: aqua;color:black;padding: 1rem;text-align: center;">
		{% if page_obj.has_previous %}
       	 <a href="?page={{ page_obj.previous_page_number }}">Previous</a>
		{% endif %}
    </li>
	<li style="display: inline;background-color: aqua;color:black;padding: 1rem;text-align: center;">
		{% if page_obj.has_next %}
     	 <a href="?page={{ page_obj.next_page_number }}">Next</a> 
    	{% endif %}
    </li>
</ul>

------------------------------
25.- Curso Django - Restframework ModelSerializer
-------------------------------
api rest framework
apps.usuario

https://www.django-rest-framework.org/



40.- Google maps
-----------------
curso de youtube
https://developers.google.com/maps/documentation/javascript/overview?hl=es#all
https://docs.djangoproject.com/en/3.1/howto/static-files/#serving-static-files-during-development
https://www.youtube.com/watch?v=BmLfvh6_vqA
31:39

python manage.py makemigrations
python manage.py migrate


google maps
https://pypi.org/project/django-google-maps/
python -m pip install django-google-maps

django-admin.py startapp googlemaps

ejemplo de github probar
https://github.com/madisona/django-google-maps/tree/master/sample


verificar este otro
https://www.pythoniza.me/mapas-desde-el-admin-django/

