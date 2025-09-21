# SoluTech Web

Proyecto Django para un sitio de servicios y tienda.

<details>
<summary><strong>Resumen</strong></summary>

- Apps principales:  
  `ServicioTecnicoApps`, `servicios`, `registro`, `contacto`, `tienda`, `carro`, `tecnico`.  
- Funcionalidad principal: gestión de servicios, tienda de productos, carrito de compras y registro de usuarios.

</details>

<details>
<summary><strong>Funcionalidades por app</strong></summary>

**servicios**
- Modelo `Servicio` con campos: `nombre`, `descripción`, `precio` e `imagen`.

**tienda**
- Modelos `CategoriaProducto` y `Producto` para listar productos.

**carro**
- Implementación de carrito en sesión (`carro/carro.py`) con funciones para: `agregar`, `restar`, `eliminar` y `limpiar`.

**registro**
- Almacenamiento básico de usuarios mediante `FormularioRegistro`.  
- Campos: `nombre_usuario`, `correo`, `password`.  
- **Nota:** no utiliza `django.contrib.auth`; las contraseñas se almacenan en texto plano.

**contacto**
- Guarda mensajes de contacto en el modelo `Contacto`.

**ServicioTecnicoApps**
- Vistas principales: `inicio` y `tienda`.

</details>

<details>
<summary><strong>Archivos relevantes</strong></summary>

- `manage.py` — punto de entrada de Django.
- `ServicioTecnico/settings.py` — configuración principal (base de datos, static/media, middleware, apps instaladas).  
- `ServicioTecnico/urls.py` — rutas principales: `servicios/`, `registro/`, `contacto/`, `tienda/`, `carro/` y raíz `/`.
- `carro/carro.py` — lógica del carrito basada en sesión.
- `tienda/models.py` y `servicios/models.py` — modelos para productos y servicios.
- `registro/models.py` y `contacto/models.py` — modelos para registro y contacto.

</details>

<details>
<summary><strong>Estructura de URLs</strong></summary>

| URL | App | Función |
|-----|-----|---------|
| `/` | ServicioTecnicoApps | Inicio |
| `/servicios/` | servicios | Listar servicios |
| `/tienda/` | tienda | Mostrar productos |
| `/carro/` | carro | Agregar, eliminar, restar, limpiar (ver `carro/urls.py`) |
| `/registro/` | registro | Registro/Login simple (ver `registro/urls.py`) |
| `/contacto/` | contacto | Formulario de contacto |

</details>

<details>
<summary><strong>Ejecutar localmente (SQLite)</strong></summary>

1. Crear y activar entorno virtual:  
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. ...