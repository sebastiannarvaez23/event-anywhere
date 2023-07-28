# Event Anywhere
Un sistema de administración de eventos el cual te permite llevar seguimientos de todos los eventos de tu negocio, empresa, o emprendimiento. Organiza tus planes de presentación, gestiona los webinar, agenda esa conferencia para tu público o también registra los eventos de tus clientes oportunamente.

## Instalación
#### Entorno virtual y dependencias
1. Lo primero que deberás hacer es crear un entorno virtual de python que te encapsule las dependencias del proyecto, ejecuta `$ python -m venv venv`, hay otras personas utilizan `$ python3 -m venv venv`, revisa cual te funciona a ti.
2. Activa el entorno virtual con el comando:
  Linux o mac: `$ source venv/bin/activate`
  Windows: `$ venv/Scripts/activate`
3. Instala las dependencias del proyecto las cuales se encuentran el archivo `requiriments.txt`. Ubicate en el proyecto al nivel del archivo mencionado y ejecuta el comando `$ pip install -r requiriments.txt`, cabe aclarar que debes asegurarte de tener el entorno virtual activado, en la mayoria de las terminales va a aparecerte (venv) sobre la linea de comando en la que estés ubicado.

De esta forma tendras las dependencias correctamente instaladas en el entorno que creaste.

## Configuración
1. Inicialmente deberás crear una base de datos denominada `events` en tu servidor de base de datos Postgresql.
2. Ubica las variables de entorno que te compartí por el correo electronico, esto añade una capa de seguridad a la aplicación. Para ello deberas descargar el archivo `.env` del correo electronico y ubicarlo al nivel de la carpeta settings. Abre el archivo y edita las variables segun las credenciales de acceso, como el dominio/ip y/o puerto al que apunta tu SBD.
3. En la terminal anterior en la que gestionamos el entorno y las dependencias, dirigite al nivel del archivo `manage.py`.
4. Luego de tener la base de datos creada, deberás crear y ejecutar las migraciones. Ejecuta el comando `$ python manage.py makemigrations` este comando te creará las migraciones. Posteriormente ejecuta el comando `$ python manage.py migrate` esto hará que los modelos de datos migren a la base que creaste en el punto 1. 
5. Por ultimo deberas ejecutar el comando `$ python manage.py runserver`.

## Uso
#### Tipo de aplicación
Esta aplicación fue construida con el framework django, utilizando la extensión de Django Rest Framework. Es una aplicación netamente de backend la cual te permitira interactuar con varios entornos. La aplicación tiene integrada una utilidad llamada Swagger, la cual te permitirá realizar peticiones sin la necesidad de utilizar Postman.

#### Herramientas de contrucción
<p align="left">
<img src="https://github.com/sebastiannarvaez23/event-anywhere/assets/88569352/d96abd89-7804-4fa5-816c-5ea41e8100ab" width="100" />
<img src="https://static-00.iconduck.com/assets.00/git-icon-1024x1024-pqp7u4hl.png" width="auto" height="90">
<img src="https://user-images.githubusercontent.com/88569352/218375255-d9a28190-10e2-44ad-b13d-721292e46815.png" width="90">
<img src="https://www.django-rest-framework.org/img/logo.png" width="180">
<img src="https://user-images.githubusercontent.com/88569352/229976087-c6d3eba8-ef91-4ff4-8260-a8f38a88093e.png" width="auto" height="80">
</p>

## Pantalla de Swagger
<img src="https://github.com/sebastiannarvaez23/event-anywhere/assets/88569352/1bbfde6d-1a94-44ab-b009-b04a85b025fa" width="500" />
