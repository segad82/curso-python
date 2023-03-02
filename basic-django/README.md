# [Curso Básico de Django](https://platzi.com/cursos/django/)
Es un framework de desarrollo web de código abierto escrito en python que respeta el patrón de diseño de software MCV.
## ¿Cómo crear un proyecto con Django?
```sh
# ~/

# 1. Crear entorno virtual
python3 -m venv env
# 2. Activar entorno virtual creado
source env/bin/activate
# 3. Instalar Django
pip3 install django
# 4. Creamos proyecto con Django
django-admin startproject <project name>
```
Esto crea la siguinete estructura de archivos y carpetas:
+ `~/<project name>/`
	+ `manage.py` Permite interactuar con los distintos comandos django.
	+ `<project name>/`
		+ `__init__.py` Permite tratar a la carpeta como un paquete en versiones anteriores de python.
		+ `asgi.py` Permite conectar proyecto a un servidor una vez realizado deploy.
		+ `settings.py` Contiene toda la configuración del proyecto django.
		+ `urls.py` Contiene las rutas del proyecto django.
		+ `wsgi.py` ¿?

```sh
# ~/<project name>/
# 5. Levantamos el servicio web del proyecto
python3 manage.py runserver
```

## Conceptos en Django

- `Proyectos`
*Estructura principal y contenedora de aplicaciones.*
- `Aplicaciones`
*Módulos de un proyecto. (ejemplo)*
*Podemos mover aplicaciones entre proyectos.*

	+ Instagram [**project**]:
		+ Feed (Foto estados) [**app**]
		+ Stories (Reels) [**app**]
		+ Messages (Chat) [**app**]
		+ ... [**app**]
		+ .. [**app**]
		+ . [**app**]

	+ Premiso Platzi App [**project**]:
		+ Polls (Encuentas) [**app**]
		+ ... [**app**]
		+ .. [**app**]
		+ . [**app**]

##### Patrón de diseño (MTV)

+ `Model:`
*Administra los datos y se usa mediante su interfaz ORM.*
+ `Template:`
*Define cómo se mostrarán la información al navegador.*
+ `View:`
*Decide qué información será mostrada y a trvés de qué plantilla.
(Intermedidor entre Model y Template)*

Aplicaciones Web

|Frontend|Backend|
| :------------: | :------------: |
|HTML|Django|
|CSS|Flask|
|Javascript|FastAPI|

Django Web

|Frontend|Backend|
| :------------: | :------------: |
|Templates|Views|

Las vistas son estructuras de python y se pueden dar de las siguientes formas:
 + `Funciones:` Function Based Views
 + `Clases:` Generic Views

### ¿Cómo crear una aplicacion en proyecto Djando?

```sh
# ~/<project name>/
# 1. Crear aplicación django
python3 manage.py startapp <app name>
```
Esto crea la siguinete estructura de archivos y carpetas:
+ `~/<project name>/<app name>`
	+ `__init__.py` Permite tratar a la carpeta como un paquete en versiones anteriores de python.
	+ `admin.py` ¿?
	+ `apps.py` ¿?
	+ `models.py` Contiene las clases del modelo ORM.
	+ `tests.py` ¿?
	+ `views.py` Contiene funciones que atienden solicitudes http.
	+ `migrations/` Almacena archivos de migración sobre el ORM.

### ¿Cómo crear el modelo ORM?

```python
# 1. Agregar en el siguiente archivo, las clases (POO) que representan las tablas en la base de datos
# ~/<project name>/<app name>/models.py
from django.db import models

class Table_Name(models.Model):
	str_column_name = models.CharField(max_length=50)
	int_column_name = models.IntegerField(default=0)
	foreign_key_column_name = models.ForeignKey(Table_FK_Name, on_delete=models.CASCADE)

# 2. Agregar aplicación al siguiente archivo, en la sección aplicaciones instaladas
# ~/<project name>/<project name>/settings.py
INSTALLED_APPS = [
	'[app name].apps.[App Name]Config',
	...
	..
	.
]
```
```sh
# ~/<project name>/

# 3. Generar archivo de migración relacionado a la aplicación
python3 manage.py makemigrations <app name>
# 4. Ejecutar archivos de migración generados (crea base de datos y tablas)
# ~/<project name>/
python3 manage.py migrate
```

### ¿Cómo podemos manipular el ORM en consola de python?
```sh
# ~/<project name>/

# 1. Ejecutamos la consola de python mediante django
python3 manage.py shell
```
```python
# Importar modelo ORM
> from <app name>.models import Table_Name

# Listar registros almacenados en la base de datos
> Table_Name.objects.all()

# Agregar registro
> x = Table_Name(column_name=value, ...)
> x.save()

# Consultar el registro con id = 1
> Table_Name.objects.get(pk=1)

# Consultar registros de un año, sobre campo [date_column_name] de tipo datetime
# Al agregar doble guión bajo al final del campo, se accede a sus sub-atributos
> from django.utils import timezone
> Table_Name.objects.get(date_column_name__year=timezone.now().year)

# Consultar registros donde un campo de texto empiece con '¿Cual'
> Table_Name.objects.filter(str_column_name__startswith="¿Cual")

# Consultar subelementos de una llave foránea mediante su conjunto [_set].
> x = Table_Name.objects.get(pk=1)
> x.fk_table_name_set.all()

# Agregar subelementos de una llave foránea mediante su conjunto [_set].
> x = Table_Name.objects.get(pk=1)
> x.fk_table_name_set.create(column_name=value, ...)
```
+ `Métodos:`
	+ `all:` retorna todos los registros del objeto ORM.
	+ `get:` retorna un registro del objeto ORM.
	+ `filter:`  retorna una lista de registros del objeto ORM. <QuerySet>
	+ `create:` crea un registro, indicando cómo parámetro, cada uno de los atributos de la tabla con su respectivo valor.
	+ `count:` retorna la cantidad de registros.
	+ `order_by:` retorna una lista de registros del objeto ORM de manera ordenada. | order_by("column_name")
+ `Subcampos de Búsqueda:`
	+ `str[__startswith]:` Empieza por
	+ `str[__endswith]:` Termina por
	+ `str[__contains]:` Contiene
	+ `str[__regex]:` Expresión regular
	+ `str|int[__in]:` Está en
	+ `int[__gt]:` Mayor que
	+ `int[__gte]:` Mayor o igual que
	+ `int[__lt]:` Menor que
	+ `int[__lte]:` Menor o igual que
	+ `any[__exact]:` Exactamente
	+ `any[__isnull]:` Es nulo
	+ `datetime[__year]:` Año
	+ `datetime[__month]:` Mes
	+ `datetime[__day]:` Día
	+ `datetime[__week]:` Semana
	+ `datetime[__week_day]:` Día de la semana
	+ `datetime[__quarter]:` Cuartíl
	+ `datetime[__time]:` Tiempo
	+ `time[__hour]:` Hora
	+ `time[__minute]:` Minuto
	+ `time[__second]:` Segundo
+ `Excepciones:`
	+ `DoesNotExist:` Ocurre cuando se intenta retornar un objeto que no existe.
	+ `MultipleObjectsReturned` Ocurre cuando la función retorna un solo registro y la condición reune más de un registro. ej. `get`

### Administrador de datos Django

#### ¿Cómo administrar datos de una entidad ORM?
```python
# 1. Registrar entidad ORM al administrador de la aplicación
# ~/<project name>/<app name>/admin.py
from django.contrib import admin
from .models import Table_Name

admin.site.register(Table_Name)
```
```sh
# ~/<project name>/

# 2. Crear super usuario en caso de no existir uno
python3 manage.py createsuperuser
# 3. Levantar servicio http
python3 manage.py runserver
# 4. Ingresar al administrador django e iniciar sesión con super usuario creado
http://127.0.0.1:8000/admin
# 5. Seleccionar entidad ORM para acceder a su mantenedor
```
 ### ¿Cómo agregar plantillas mediante Function Based Views?
```sh
# ~/<project name>/<app name>/

# 1. Crear carpeta 'templates' y supcarpeta de la aplicación
mkdir templates
cd templates
mkdir <app name>
# 2. Crear plantilla html (consultar lenguaje django-html)
# ~/<project name>/<app name>/templeates/<app name>/index.html (ejemplo)
```
```python
# 3. Agregar funcion a la vista de la aplicación que atienda la solicitud http
# ~/<project name>/<app name>/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, '<app name>/index.html', { parameter: value })
	
def index_with_parameter(request, parameter):
	return HttpResponse(f"El parámetro es: {parameter}")

# 4. Agregar url a la aplicación.
# ~/<project name>/<app name>/urls.py
from django.urls import path
from . import views
urlpatterns = [
	path('', views.index, name='index'),
	path('<str:parameter>/', views.index_with_parameter, name='index_with_parameter'),
	...
	..
	.
]

# 5. Agregar las url de la aplicación al proyecto
# ~/<project name>/<project name>/urls.py
from django.urls import path, include
 urlpatterns = [
 	path('<app name>/', include('<app name>.urls')),
	...
	..
	.
]

# 6. Ingresar a la url desde el navegador
http://127.0.0.1:8000/<app name>
```
Nota: Para tener mejor usabilidad sobre las django templates con Visual Studio Code, hacemos lo siguiente.
1. En Visual Studio Code, presionar [Ctrl] + [Shift] + [p]
2. En la barra, escribir settings.json e ingresar a él
3. Agregar al archivo lo siguiente.
`"emmet.includeLanguages": { "django-html": "html" }` ó `"emmet.includeLanguages": { "html": "django-html" }`
4. Instalar extención Django by 'Baptiste Darthenay' en Visual Studio Code

### ¿Cómo escalar error 404 en las vistas?
```python
# 1. Desde la vista de la aplicación, importar función [get_object_or_404] de [django.shortcuts]
# ~/<project name>/<app name>/views.py
from django.shortcuts import render, get_object_or_404
from .models import Table_Name

def index_with_parameter(request, parameter):
    object = get_object_or_404(Table_Name, pk=parameter)
    return render(request, 'polls/file.html', { 'object': object })
```

### Mejorar el manejo de urls en plantillas

```python
# 1. Desde las urls de la aplicación, definir la variable [app_name] con el nombre de la aplicación.
# ~/<project name>/<app name>/urls.py
from django.urls import path
from . import views
app_name = '<app name>'
urlpatterns = [ 
	path('url', views.function_name, name='url_name'),
	path('<str:parameter>/', views.function_with_parameter, name='url_with_parameter'),
	...
	..
	.
]
```
```html
# 2. Invocar url mediante su nombre
# ~/<project name>/<app name>/templates/<app name>/file.html
<a href="{% url '<app_name>:<url_name>' %}">
<a href="{% url '<app_name>:<url_with_parameter>' parameter %}">
```
Para mayor información sobre el lenguaje de plantillas django.
https://docs.djangoproject.com/en/4.0/ref/templates/language/
https://docs.djangoproject.com/en/4.0/ref/templates/builtins/

### [¿Cómo agregar plantillas mediante Generic Views?](https://ccbv.co.uk/)
```sh
# ~/<project name>/<app name>/

# 1. Crear carpeta 'templates' y supcarpeta de la aplicación en caso de no existir
mkdir templates
cd templates
mkdir <app name>
# 2. Crear plantilla html (consultar lenguaje django-html)
# ~/<project name>/<app name>/templeates/<app name>/index.html (ejemplo)
```
```python
# 3. Agregar funcion a la vista de la aplicación que atienda la solicitud http
# ~/<project name>/<app name>/views.py
from django.views import generic
from .models import Table_Name

class IndexView(generic.ListView):
	template_name = '<app name>/index.html'
	context_object_name = 'parameter_name'
	
	def get_queryset(self):
		return Table_Name.objects.all()
class CustomDetailView(generic.DetailView):
	model = Table_Name
	template_name = '<app name>/file.html'

# 4. Agregar url a la aplicación.
# ~/<project name>/<app name>/urls.py
from django.urls import path
from . import views
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<str:column_name>/', views.CustomDetailView.as_view(), name='custom_detail'),
	...
	..
	.
]

# 5. Agregar las url de la aplicación al proyecto
# ~/<project name>/<project name>/urls.py
from django.urls import path, include
urlpatterns = [
	path('<app name>/', include('<app name>.urls')),
	...
	..
	.
]

# 6. Ingresar a la url desde el navegador
http://127.0.0.1:8000/<app name>
```

> Esto fue editado desde [Editor.md](https://pandao.github.io/editor.md/en.html).