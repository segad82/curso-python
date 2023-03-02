# [Curso de Python: PIP y Entornos Virtuales](https://platzi.com/cursos/python-pip/)

## PIP
Es el manejador de paquetes de python. (ver paquetes soportados [aquí](https://pypi.org/))

```python
# Instala un paquete python.
pip install <package name>

# Instala una versión de paquete python en específico.
pip install <package name>==<version number>

# Muestra el listado de librerias python instaladas.
pip freeze
```
## Maneras de Trabajar con Python
### Entorno Python
Al instalar python, automaticamente se crea un entorno global donde se puede empezar a instalar dependencias que impactan a todos los proyectos de la máquina.

Esto significa un problema ya que pueden existir conflictos de dependencias entre proyectos de la misma máquina.

Considerar que.
```python
# Este comando nos indica desde donde se ejecuta otro comando.
which <command>
 
# Podemos revisar desde donde ejecuta python o pip
which python3 # /usr/bin/python3 (ambiente global)
which pip3 # /usr/bin/pip3 (ambiente global)
```
Para solucionarlo, se pueden encapsular los proyectos en entornos virtuales independientes.
#### Entornos Virtuales
Permite generar espacios de trabajo por cada proyecto, donde las dependencias python se mantienen separadas, evitando conflicto de versiones sobre las dependencias de distintos proyectos.

El paquete que nos permite trabajar con entornos virtuales de python es **python3-venv**.

Una vez esté instalado, nos ubicamos en la carpeta raiz del proyecto y hacemos lo siguiente:
```sh
# Crear entorno virtual | Por convención se utiliza 'env' como nombre de entorno virtual.
python3 -m venv <virtual environment name>
# Activar entorno virtual.
source env/bin/activate
# Consultar entorno donde se ejecuta python y validamos que lo hace desde el virtual.
which python3
# Generar archivo con dependencias python | Por convención se utiliza 'requirements.txt'
pip3 freeze > requirements.txt
# Desactivar entorno vurtual.
deactivate
```
Exportar las dependencias de python al archivo `requirements.txt` permite dejar instrucciones simples en el archivo `README.md` para que otros puedan preparar su entorno de python y colaborar en el proyecto.
#### > Ejemplo: Proyecto App
```sh
git clone https://github.com/segad82/curso-python.git
cd pip-virtual-environments/app
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py
```
### Contenedores Doker
Separa completamente los espacios de trabajo.

Para usarlo, primero se debe instalar:
- [Docker Engine](https://docs.docker.com/engine/install/debian/)
- [Docker Desktop](https://docs.docker.com/desktop/install/ubuntu/)

Una vez instalado.
```sh
# Abrimos Docker Desktop
systemctl --user start docker-desktop
# Creamos el contenedor en función del archivo 'docker-compose.yml'
docker-compose build
# Listamos los contenedores construidos para ver su estado
docker-compose ps
# Iniciamos el contenedor a través de un daemon
docker-compose up -d
# Ingresamos a un contenedor por consola (bash). <service name> está definido en el archivo 'docker-compose.yml'
docker-compose exec <service name> bash
```
#### > Ejemplo: Proyecto App
```sh
git clone https://github.com/segad82/curso-python.git
cd pip-virtual-environments/app
systemctl --user start docker-desktop
docker-compose build
docker-compose up -d
docker-compose exec app-csv bash
```
#### > Ejemplo: Proyecto Web Server
```sh
git clone https://github.com/segad82/curso-python.git
cd pip-virtual-environments/web-server
systemctl --user start docker-desktop
docker-compose build
docker-compose up -d
docker-compose ps
firefox http://localhost:80/web
```
> Esto fue editado desde [Editor.md](https://pandao.github.io/editor.md/en.html).