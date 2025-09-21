**Resumen**
- Proyecto Django para un sitio de servicios y tienda (SoluTech Web).
- Apps principales: `ServicioTecnicoApps`, `servicios`, `registro`, `contacto`, `tienda`, `carro`, `tecnico`.

**Qué hace**
- `servicios`: modelo `Servicio` con nombre, descripción, precio e imagen.
- `tienda`: modelos `CategoriaProducto` y `Producto` para listar productos.
- `carro`: implementación de carrito en sesión (`carro/carro.py`) con funciones para agregar, restar, eliminar y limpiar.
- `registro`: almacenamiento básico de usuarios mediante el modelo `FormularioRegistro` (no usa el sistema `django.contrib.auth` para registros), contiene `nombre_usuario`, `correo` y `password`.
- `contacto`: guarda mensajes de contacto en el modelo `Contacto`.
- `ServicioTecnicoApps`: vistas principales para `inicio` y `tienda`.

**Archivos relevantes**
- `manage.py:1` — punto de entrada de Django (usa `ServicioTecnico.settings`).
- `ServicioTecnico/settings.py:1` — configuración principal (base de datos, static/media, middleware, apps instaladas).
- `ServicioTecnico/urls.py:1` — rutas principales: `servicios/`, `registro/`, `contacto/`, `tienda/`, `carro/` y la ruta raíz.
- `carro/carro.py:1` — lógica del carrito basada en sesión.
- `tienda/models.py:1` y `servicios/models.py:1` — modelos para productos y servicios.
- `registro/models.py:1` y `contacto/models.py:1` — modelos para registro y contactos.

**Estructura de URLs (resumen)**
- `/` → app `ServicioTecnicoApps` (`inicio`).
- `/servicios/` → app `servicios`.
- `/tienda/` → app `tienda` (muestra productos).
- `/carro/` → endpoints para `agregar`, `eliminar`, `restar`, `limpiar` (ver `carro/urls.py`).
- `/registro/` → endpoints de registro/login simples (ver `registro/urls.py`).
- `/contacto/` → formulario de contacto.

**Cómo ejecutar (local, usando SQLite)**
- Crear y activar un entorno virtual (recomendado): `python3 -m venv .venv` y `source .venv/bin/activate`.
- Instalar dependencias: `pip install -r requirements.txt` (si no se usa, instalar al menos `Django` y dependencias que el proyecto requiera).
- Ejecutar migraciones: `python3 manage.py migrate`.
- (Opcional) Crear superusuario: `python3 manage.py createsuperuser`.
- Iniciar servidor de desarrollo: `python3 manage.py runserver`.

Nota: la configuración en `ServicioTecnico/settings.py:1` usa `dj_database_url` con `DATABASE_URL` por defecto y cae a SQLite (`db.sqlite3`) si no hay otra configuración.

**Static y Media**
- `STATIC_URL` = `/static/`, `STATIC_ROOT` = `staticfiles` y `STATICFILES_DIRS` incluye `static`.
- `MEDIA_URL` = `/media/`, `MEDIA_ROOT` = `media`.
- `whitenoise` está configurado en `MIDDLEWARE` y `STATICFILES_STORAGE` para servir estáticos en despliegue sencillo.

**Notas importantes / recomendaciones**
- `DEBUG` en `ServicioTecnico/settings.py:1` está en `False`; para desarrollo puede activarse a `True`.
- El registro actual guarda contraseñas en texto plano en `registro.models.FormularioRegistro` — cambiar a `django.contrib.auth` o al menos hashear contraseñas para producción.
- `registro` implementa login manual; revisar/usar `django.contrib.auth` para seguridad y funciones completas.
- `ALLOWED_HOSTS` está en `['*']`; ajustar para producción.
- `requirements.txt` puede necesitar revisión (asegurar codificación legible y versiones correctas).

Heroku / despliegue (nota):
- Este proyecto tenía una configuración para Heroku (Procfile). Se ha eliminado del repositorio por claridad; abajo hay un ejemplo comentado de `Procfile` si quieres usarlo más adelante.

Procfile (ejemplo comentado):
# web: gunicorn ServicioTecnico.wsgi

Variables de entorno y base de datos:
- Añadir un archivo `.env` en la raíz con las variables mínimas (`SECRET_KEY`, `DEBUG`, `DB_ENGINE`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`).
- Para usar MySQL: poner `DB_ENGINE=True` y rellenar las demás variables. Por defecto `DB_ENGINE=False` y se usa `SQLite3`.

Archivo de ejemplo: `.env.example` incluido en el repo.
