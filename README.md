# Tarea Semana 15 - Manejo de eventos en restaurante_app

## Descripción

En esta tarea de la Semana 15 continué trabajando en el sistema de restaurante que he venido desarrollando durante las semanas anteriores.

El objetivo principal de esta semana fue aplicar los fundamentos del manejo de eventos en una interfaz gráfica con Tkinter. Para ponerlo en práctica agregué una sección de ventas, donde se puede seleccionar un usuario y un producto que ya estén registrados y luego realizar el registro de la venta mediante un botón.

Para realizar esta actividad no hice un proyecto nuevo desde cero. Trabajé sobre la aplicación de la semana anterior y mantuve la organización que ya tenía en datos, modelos, servicios e interfaz.

## Evolución del proyecto

En la versión anterior del sistema ya tenía implementado el inicio de sesión, la navegación de la aplicación, la gestión de productos y la consulta de usuarios.

Para la Semana 15 continué con el mismo proyecto y agregué lo necesario para trabajar con ventas y eventos.

Los principales cambios que realicé fueron:

- Incorporé el modelo `Venta`.
- Agregué el archivo `ventas.json`.
- Incorporé una nueva sección llamada Ventas.
- Permití seleccionar un usuario registrado.
- Permití seleccionar un producto registrado.
- Agregué el botón Registrar venta.
- Utilicé `command=` para relacionar el botón con su callback.
- El registro de la venta se realiza mediante `RestauranteServicio`.
- Las ventas registradas se muestran en una tabla.
- Las ventas quedan guardadas y se recuperan cuando se vuelve a iniciar el programa.
- Incorporé la carpeta `assets` con el logo y los íconos del sistema.

De esta forma pude agregar la nueva funcionalidad sin eliminar lo que ya funcionaba en las semanas anteriores.

## Estructura del proyecto

El proyecto mantiene una estructura modular para que cada parte tenga una función específica.

```text
restaurante_app/
│
├── assets/
│   ├── logo.png
│   ├── logo_app.png
│   ├── productos.png
│   ├── productos_icon.png
│   ├── usuarios.png
│   ├── usuarios_icon.png
│   ├── ventas.png
│   └── ventas_icon.png
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
└── main.py
```

La carpeta `datos` contiene los archivos JSON utilizados para guardar la información.

En `modelos` se encuentran las clases principales del sistema, como Producto, Usuario y Venta.

En `servicios` se encuentra la lógica utilizada para trabajar con los datos y realizar las operaciones del restaurante.

En `ui` se encuentran las ventanas y componentes gráficos desarrollados con Tkinter.

La carpeta `assets` contiene el logo y los íconos que se utilizan en la interfaz.

Finalmente, `main.py` es el archivo utilizado para iniciar la aplicación.

## Gestión de ventas

Para esta semana agregué una sección de Ventas que permite relacionar un usuario con un producto.

Primero se selecciona un usuario registrado y después se selecciona un producto registrado. Cuando se presiona el botón Registrar venta, el sistema toma esas selecciones y solicita a `RestauranteServicio` que realice el registro.

Cada venta guarda la siguiente información:

- Usuario.
- Producto.
- Fecha del registro.

Después de registrar la venta, la tabla se actualiza y permite visualizar el nuevo registro.

También realicé la prueba de cerrar completamente la aplicación y volver a ejecutarla. Las ventas registradas anteriormente volvieron a aparecer, comprobando que la información se mantiene guardada.

## Manejo de eventos

En esta actividad utilicé el parámetro `command=` de Tkinter para trabajar el manejo de eventos solicitado en la Semana 15.

En el botón Registrar venta se utiliza:

```python
command=self.registrar_venta
```

Esto permite que al presionar el botón se ejecute el método `registrar_venta`, que funciona como callback.

El callback obtiene el usuario y el producto seleccionados en la interfaz. Luego envía esa información a `RestauranteServicio`, que se encarga de realizar la operación correspondiente.

El flujo que utilicé es el siguiente:

```text
Usuario
   ↓
Botón Registrar venta
   ↓
command=
   ↓
Callback registrar_venta
   ↓
RestauranteServicio
   ↓
ventas.json
   ↓
Actualización de la tabla
   ↓
Respuesta en la interfaz
```

De esta manera la interfaz se encarga de recibir la acción del usuario y mostrar el resultado, mientras que la operación de la venta se delega al servicio.

## Persistencia de las ventas

Las ventas se guardan en el archivo:

```text
restaurante_app/datos/ventas.json
```

La interfaz no escribe directamente en este archivo. Para mantener organizada la aplicación, la lectura y escritura de los datos se realiza mediante los servicios del sistema.

Cuando se registra una venta, esta se almacena en `ventas.json`. Cuando la aplicación se vuelve a iniciar, los datos guardados se cargan nuevamente.

Esto permite conservar las ventas aunque el programa sea cerrado.

## Interfaz gráfica

La aplicación continúa utilizando Tkinter y ttk para la interfaz gráfica.

Se mantuvieron las secciones de Productos y Usuarios y se agregó la sección de Ventas.

Para mejorar la presentación también incorporé la carpeta `assets`, donde se encuentran los recursos visuales utilizados por la aplicación.

Actualmente se utiliza:

- Logo del Sistema de Restaurante.
- Ícono de Productos.
- Ícono de Usuarios.
- Ícono de Ventas.

Los botones del menú permiten navegar de forma sencilla entre las diferentes secciones del sistema.

En la sección de Ventas se utilizan listas de selección para escoger el usuario y el producto, un botón para registrar la venta y una tabla para visualizar los registros realizados.

## Ejecución del programa

Para ejecutar el proyecto se debe tener instalado Python 3.

Primero se debe abrir una terminal en la carpeta principal del proyecto.

Después se ejecuta:

```bash
python restaurante_app/main.py
```

En Windows también se puede utilizar:

```powershell
python restaurante_app\main.py
```

Al ejecutar `main.py` se abre la aplicación del Sistema de Restaurante.

Después de iniciar sesión se puede navegar entre las secciones de Productos, Usuarios y Ventas.

## Pruebas realizadas

Antes de finalizar la tarea realicé varias pruebas para comprobar que los cambios realizados funcionaran correctamente.

Probé lo siguiente:

- Ejecución de `main.py` sin errores.
- Inicio de sesión.
- Cierre de sesión.
- Navegación entre Productos, Usuarios y Ventas.
- Visualización de los productos registrados.
- Visualización de los usuarios registrados.
- Selección de un usuario para realizar una venta.
- Selección de un producto para realizar una venta.
- Registro mediante el botón Registrar venta.
- Ejecución del callback mediante `command=`.
- Actualización de la tabla después de registrar una venta.
- Almacenamiento de la venta en `ventas.json`.
- Cierre completo de la aplicación.
- Nueva ejecución del programa para comprobar que las ventas continúan guardadas.
- Visualización del logo y los íconos almacenados en la carpeta `assets`.

Las pruebas realizadas permitieron comprobar que las funciones anteriores continúan trabajando y que la nueva sección de Ventas se encuentra integrada al sistema.

## Conclusión

Con esta actividad pude entender de una manera más práctica cómo funciona el manejo de eventos en una interfaz gráfica.

En el sistema, cuando el usuario presiona el botón Registrar venta, se ejecuta un callback mediante `command=`. Este callback obtiene la información seleccionada y solicita al servicio que realice el registro. Después la interfaz se actualiza para mostrar el resultado.

También pude continuar mejorando el mismo proyecto de las semanas anteriores sin cambiar su estructura principal. En esta semana agregué la gestión de ventas, la persistencia en `ventas.json` y los recursos visuales del sistema, manteniendo separadas la interfaz, la lógica y el manejo de los datos.