# 2024-2-Grupo-6: PROYECTO WC FINDER
# Ingeniería de Software CC4401-2 Otoño 2024
**Integrantes**: 
- Ignacio Humire
- Ignacio Gajardo
- Julieta Ayelli
- Fernanda Contreras
- Cristóbal Pereira
- Diego Tapia
---
## El proyecto
WC FINDER es una aplicación web móvil (pricipamente), que permite a los estudiantes encontrar un baño de acuerdo a sus necesidades o preferencias. 
## Para iniciar el proyecto
### Repositorio
Para comenzar debemos clonar el repositorio o descargarlo.
```bash
git clone https://github.com/DCC-CC4401/2024-1-CC4401-2-grupo-6.git
```
Luego se debe acceder a la carpeta ya sea esta clonada o descargada.
### Creación del ambiente virtual
Creamos un ambiente virtual de python y lo incializamos.
```bash
python -m venv env
env\Scripts\activate
```
### Configuración del ambiente virtual
Actualizamos pip.
```bash
python -m pip install --upgrade pip
```

Instalamos las librerías requeridas para el funcionamiento del proyecto.

```bash
pip install -r requirements.txt
```
Para actualizar
```bash
python manage.py makemigrations
python manage.py migrate
```

Para iniciar
```bash
python manage.py runserver  
```
## Sprint 1
Fecha de término: 22-05-2024
### Notas de versión:
-  Se implementó el esqueleto de una aplicación web con django
- Se implementaron las vistas /register , /login y /tareas.
- Se implementó la funcionalidad para que usuario se pueda registrar
- Se implementó la funcionalidad para que un usuario se logee.
- Se implementó la funcionalidad para que un usuario logeado pueda enviar un formulario.

### Implementaciones futuras
- Acción de aceptar solicitudes de formularios en el perfil de administrador.
- Agregar opciones y características al formulario.
- Cambios en diseño registro y formulario
