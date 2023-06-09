## Descripción del proyecto
El aplicativo es el encargado de actuar como API contra el aplicativo de la tienda del proyecto de moviles 2
Tiene implementado autorizacion por medio de Oauth2.0
## Configuración de entorno de desarrollo

Las siguientes instrucciones tienen como objetivo que puedas configurar tu ambiente de desarrollo en Ubuntu 20 dentro de Windows con [WSL](https://docs.microsoft.com/en-us/windows/wsl/install) o [Vagrant](https://www.vagrantup.com/downloads).  Recomendamos usar [<img src="http://img.shields.io/badge/-VS%20Code-007ACC?style=flat&logo=visual%20studio%20code&logoColor=white">](https://code.visualstudio.com/)

### Instalar prerequisitos en Ubuntu

Instalacion del entorno vierutal en este caso pyenv
```sh
$  curl https://pyenv.run | bash

# Configuracion de variables de entorno para permitir el uso de pyenv

$ export PATH="$HOME/.pyenv/bin:$PATH"
$ eval "$(pyenv init -)"
$ eval "$(pyenv virtualenv-init -)"
$ exec "$SHELL"
```


### Configurar PostgreSQL en Ubuntu
- Para permitir autenticación peer sigue las instrucciones del siguiente enlace :arrow_right: [PostgreSQL Configuration](https://stackoverflow.com/questions/18664074/)
- Crear en postgresql una base de datos con el nombre **shopAppBd**

Nota: La sentencia de conexion y usuarios estan sobre las variables de entorno

### Crear ambiente para desarrollo en Python3

```sh
# Instalar ultima version de Python
$ pyenv install 3.11.3
# Crear ambiente
$ pyenv virtualenv 3.11.3 appStoreApi
# Activar ambiente
$ pyenv activate appStoreApi
# Desactivar ambiente (Cuando sea necesario)
$ deactivate
```
### Instalar librerías del proyecto
```sh
# las librerías se deben instalar después de haber activado el ambiente
$(env) pip install -r requirements.txt
```


### Variables de Entorno necesarias

```sh
DEBUG=True --> Habilitacion del modo Debug de Django
DATABASE_URL=postgres://username:password@host:port/dbname -> Aqui se puede usar cualquier sentencia para base de datos del paquete dj-database-url ver mas:  [https://pypi.org/project/dj-database-url/](dj-database-url)
DJANGO_LOG_LEVEL=INFO --> Nivel de Log en Django recomentado INFO
ROOT_LOG_LEVEL=DEBUG --> Nivel de Log de python recomentado DEBUG en entorno local para visualizar
```

Uso de variable de entorno en entorno local

1. Crear el archivo .env en la carpeta raiz, y configurar las variables necesarias
2. Modificar el archivo settings.py y adicionar la siguiente lineas al inicio
```sh
from dotenv import load_dotenv
load_dotenv()
```
3. Validar que se tenga instalado el paquete python-dotenv en pip

## Iniciar el proyecto por primera vez
1. Crear y aplicar las migraciones a las que haya lugar y luego correr el proyecto
```sh
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```

2. Como no tenemos un copia de base de datos se debe de crear un super usuario inicial
```sh
$ python3 manage.py createsuperuser
```

> Ir a: [http://127.0.0.1:8000/](http://127.0.0.1:8000/) para ver el proyecto en ejecución.
> Ir a: [http://127.0.0.1:8000/secret](http://127.0.0.1:8000/secret) para acceder la panel de administración del proyecto

### Uso de la API
Para poder probar la api del proyecto deberás instalar [Postman](https://www.postman.com/downloads/) e importar las colecciones correspondientes las cuales estan ubicadas en la carpeta [./others/collections/](./others/collections/). 
En esta colección encontrarás todos los request necesarios para hacer pruebas locales de la app.

:bulb: Los endpoints de CART y PRODUCTS cuentan con la configuracion estandar de ModelViewSet de DRF, por lo cual aceptan request GET, POST, PUT, PATH, DELETE

### Uso de la API
La API tiene implementado autenticacion con OAUTH por lo cual al iniciar el servidor se debe de crear las aplicacion permitidas.

Ir a : [http://127.0.0.1:8000/api/user/o/applications/](http://127.0.0.1:8000/api/user/o/applications/)

Registrar la aplicacion con el flujo de Oauth deseado, de resto toda la autenticacion respeta el estandar de oauth, siendo el endpoint raiz [http://127.0.0.1:8000/api/user/o/](http://127.0.0.1:8000/api/user/o/)

:bulb: Para el caso de angular recomiento Resource owner password-based para implementar un login
:bulb: Guardar client_id y client_secret
