# Proyecto Final Coder House - Python

**Comisión**: 56070  
**Alumno**: Daniela Gangotena

## Nombre del Proyecto: 
**Blog de publicaciones entre usuarios**

### Versión:
1.0

## Descripción del Proyecto

Este proyecto es una **Página Web** destinada a usuarios que deseen publicar sus opiniones o ideas en un blog. Los usuarios pueden registrarse, escribir publicaciones, ver publicaciones de otros usuarios, y comunicarse mediante un sistema de mensajería.

### Funcionalidades

La aplicación cuenta con las siguientes funcionalidades principales:

- **Barra de navegación**: Permite acceder a las diferentes secciones del sitio.
- **Login/Registrarse/Logout**: Los usuarios pueden registrarse en la plataforma, iniciar sesión y cerrar sesión.
- **Registro de usuario**: Los usuarios pueden crear su cuenta completando un formulario.
- **Ver usuarios**: Se muestra una lista de usuarios registrados, y se puede ver el perfil de un usuario individual.
- **Ver publicaciones**: Los usuarios pueden ver las publicaciones de otros y buscar publicaciones por título.
- **Ver publicación individual**: Los usuarios pueden ver una publicación en detalle y agregar comentarios.
- **Escribir publicaciones**: Los usuarios registrados pueden escribir y publicar sus propias publicaciones.
- **Mensajería**: Los usuarios pueden chatear con otros usuarios, incluido el administrador.

## Tecnologías Utilizadas

### Front-End:
- **HTML**: Para la estructura de la página web.
- **CSS**: Para el estilo y diseño de la interfaz.
- **JavaScript ES6**: Para la interactividad del sitio.
- **Bootstrap**: Para el diseño responsivo y los componentes predefinidos.

### Back-End:
- **Python**: Lenguaje de programación utilizado para el desarrollo del servidor.
- **Django**: Framework de desarrollo web utilizado en el backend.

## Instrucciones de Instalación

Para poder ejecutar el proyecto en tu máquina local, sigue estos pasos:

### 1. Clonar el repositorio
Primero, clona el repositorio del proyecto en tu máquina local:
```bash
git clone https://github.com/dggtn9/PlaygroundFinalProjectGangotena.git
2. Crear un entorno virtual
Es recomendable crear un entorno virtual para instalar las dependencias necesarias:

bash
Copiar código
cd PlaygroundFinalProjectGangotena
python -m venv venv
3. Activar el entorno virtual
Para activar el entorno virtual:

En Windows:
bash
Copiar código
venv\Scripts\activate
En macOS/Linux:
bash
Copiar código
source venv/bin/activate
4. Instalar las dependencias
Instala las dependencias del proyecto con pip:

bash
Copiar código
pip install -r requirements.txt
5. Configurar la base de datos
Ejecuta las migraciones para configurar la base de datos:

bash
Copiar código
python manage.py migrate
6. Ejecutar el servidor de desarrollo
Levanta el servidor de desarrollo de Django:

bash
Copiar código
python manage.py runserver
Ahora puedes acceder a la aplicación en tu navegador en la siguiente URL:

arduino
Copiar código
http://127.0.0.1:8000
Pruebas Realizadas
Puedes revisar las pruebas realizadas en el archivo titulado "Pruebas Proyecto Python CH.xlsx" que se encuentra en el repositorio. Este archivo contiene una lista de las pruebas realizadas durante el desarrollo del proyecto.

Repositorio con archivo de pruebas: Pruebas Proyecto Python CH.xlsx
Video Demostración
Para ver una demostración en video del proyecto, puedes acceder al siguiente enlace:

Video Demostración

Contribuciones
Si deseas contribuir a este proyecto, sigue estos pasos:

Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y haz commit (git commit -am 'Agrega nueva funcionalidad').
Empuja los cambios a tu repositorio (git push origin feature/nueva-funcionalidad).
Abre un pull request en el repositorio original.
Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

