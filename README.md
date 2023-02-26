# Cursos de Python en Platzi
Este repositorio lo utilizo para almacenar los ejemplos y apuntes tomados en los siguientes cursos de Python en Platzi.
- [Comprehensions, Funciones y Manejo de Errores](https://platzi.com/cursos/python-funciones/)
- [PIP y Entornos Virtuales](https://platzi.com/cursos/python-pip/)

### Ejemplos
```sh
# Juego de piedra papel o tijera.
python3 comprehensions-functions-errorhandler/11_game.py

# Gráfico de torta (a,b,c) con números aleatorios.
python3 comprehensions-functions-errorhandler/app/charts.py

# Gráfico poblacional de Colombia según archivo csv descargado de kaggle.com
python3 comprehensions-functions-errorhandler/app/challenge_1.py

# Gráfico poblacional de los países en sur américa según archivo csv descargado de kaggle.com
python3 comprehensions-functions-errorhandler/app/challenge_2.py
```

##Maneras de Trabajar con Python
###Entornos Virtuales
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
#### > Ejemplo: Proyecto Web Server
```sh
git clone https://github.com/segad82/curso-python.git
cd pip-virtual-environments/web-server
systemctl --user start docker-desktop
docker-compose build
docker-compose up -d
docker-compose exec <service name> bash
```
> Esto fue editado desde [Editor.md](https://pandao.github.io/editor.md/en.html).
