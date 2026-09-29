# Tarea Semana 15 - Manejo de eventos en restaurante_app

## Descripción

En esta tarea de la Semana 15 continué trabajando en el Sistema de Restaurante que he venido desarrollando durante las semanas anteriores.

El objetivo principal de esta semana fue comprender y aplicar los fundamentos básicos del manejo de eventos utilizando Tkinter. Para poner en práctica este tema agregué una nueva sección de Ventas, donde se puede seleccionar un usuario y un producto que ya estén registrados y realizar una venta mediante un botón.

No realicé un proyecto nuevo desde cero. Continué trabajando sobre la aplicación de la semana anterior, conservando el inicio de sesión, la gestión de productos, la consulta de usuarios, la persistencia mediante archivos JSON y la organización del proyecto en diferentes módulos.

## Evolución del proyecto

En la versión anterior del sistema ya tenía implementado el inicio de sesión, la navegación principal, la gestión de productos y la consulta de usuarios.

Para la Semana 15 continué con el mismo proyecto y agregué lo necesario para trabajar con ventas y manejo de eventos.

Los principales cambios realizados fueron:

- Incorporación del modelo `Venta`.
- Creación del archivo `ventas.json`.
- Incorporación de una nueva sección de Ventas.
- Selección de un usuario registrado.
- Selección de un producto registrado.
- Botón **Registrar venta**.
- Uso de `command=` para relacionar el botón con un callback.
- Registro de la venta mediante `RestauranteServicio`.
- Visualización de las ventas registradas en una tabla.
- Actualización de la tabla después de registrar una venta.
- Persistencia de las ventas para recuperarlas al volver a ejecutar el programa.
- Incorporación de la carpeta `assets` con el logo y los íconos utilizados por el sistema.

De esta manera pude incorporar la nueva funcionalidad sin eliminar ni reemplazar las funciones que ya tenía desarrolladas.

## Estructura del proyecto

El proyecto mantiene una estructura modular para separar las diferentes responsabilidades del sistema.

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

La carpeta `datos` contiene los archivos JSON utilizados para guardar la información del sistema.

En `modelos` se encuentran las clases principales: Producto, Usuario y Venta.

En `servicios` se encuentra la lógica utilizada para realizar las operaciones y trabajar con los datos.

En `ui` se encuentran las vistas y los componentes gráficos desarrollados con Tkinter.

La carpeta `assets` contiene el logo y los íconos utilizados en la interfaz.

Finalmente, `main.py` es el punto de entrada utilizado para iniciar la aplicación.

## Gestión de ventas

Para esta semana agregué una sección de Ventas que permite relacionar un usuario registrado con un producto existente.

Primero se selecciona el usuario y después el producto. Al presionar el botón **Registrar venta**, la interfaz obtiene estas selecciones y solicita a `RestauranteServicio` que realice la operación.

Cada venta almacena:

- Usuario.
- Producto.
- Fecha del registro.

Antes de registrar la venta, el servicio comprueba que el usuario y el producto seleccionados existan.

Después de realizar correctamente la operación, la tabla de ventas se actualiza para mostrar el nuevo registro al usuario.

Las ventas también se guardan en `ventas.json`, por lo que pueden recuperarse cuando se cierra y se vuelve a ejecutar la aplicación.

## Manejo de eventos

En esta actividad utilicé `command=` de Tkinter para aplicar el fundamento de manejo de eventos estudiado durante la Semana 15.

En el botón **Registrar venta** se utiliza:

```python
command=self.registrar_venta
```

De esta manera, cuando el usuario presiona el botón se ejecuta el método `registrar_venta`, que funciona como callback.

El callback obtiene el usuario y el producto seleccionados en la interfaz y solicita a `RestauranteServicio` que realice el registro.

El flujo aplicado es:

```text
Usuario realiza una acción
        ↓
Botón Registrar venta
        ↓
command=
        ↓
Callback registrar_venta
        ↓
RestauranteServicio
        ↓
Persistencia en ventas.json
        ↓
Actualización de la tabla
        ↓
Respuesta en la interfaz
```

De esta forma la interfaz coordina la interacción con el usuario, mientras que las validaciones y la operación de la venta se mantienen dentro del servicio.

## Persistencia de las ventas

Las ventas registradas se almacenan en:

```text
restaurante_app/datos/ventas.json
```

La interfaz no lee ni escribe directamente este archivo.

La operación se delega a los servicios del sistema, manteniendo separada la interfaz de la lógica y de la persistencia de los datos.

Cuando se registra una venta, la información queda almacenada en `ventas.json`. Al cerrar y volver a ejecutar la aplicación, las ventas guardadas se cargan nuevamente.

## Interfaz gráfica

La aplicación utiliza Tkinter y ttk para construir la interfaz gráfica.

Se mantienen las secciones desarrolladas anteriormente:

- Productos.
- Usuarios.

Y para esta semana se incorporó:

- Ventas.

En la sección de Ventas se utilizan componentes de selección para escoger un usuario y un producto, un botón para registrar la operación y una tabla para visualizar las ventas realizadas.

También incorporé la carpeta `assets`, donde se encuentran los recursos visuales utilizados por la aplicación:

- Logo del Sistema de Restaurante.
- Ícono de Productos.
- Ícono de Usuarios.
- Ícono de Ventas.

Estos elementos permiten mantener una presentación más clara y organizada en las diferentes secciones del sistema.

## Acceso a la aplicación

Para facilitar la revisión y prueba del proyecto se pueden utilizar las siguientes credenciales:

```text
Usuario: Dennis
Contraseña: 1234
```

Estas credenciales permiten ingresar a la aplicación y acceder a las secciones de Productos, Usuarios y Ventas.

## Ejecución del programa

Para ejecutar el proyecto se debe tener instalado Python 3.

Primero se debe abrir una terminal en la carpeta del repositorio:

```text
Tarea-Semana-15-Restaurante-Eventos
```

Después ingresar a la carpeta de la aplicación:

```powershell
cd restaurante_app
```

Finalmente ejecutar:

```powershell
python main.py
```

También se puede ejecutar directamente desde la carpeta principal del repositorio utilizando:

```powershell
python restaurante_app\main.py
```

Al ejecutar `main.py` se abrirá la pantalla de acceso del Sistema de Restaurante.

Después se pueden utilizar las credenciales indicadas anteriormente para ingresar y navegar por las secciones de Productos, Usuarios y Ventas.

## Pruebas realizadas

Para comprobar el funcionamiento del proyecto realicé las siguientes pruebas:

- Ejecución de `main.py`.
- Inicio de sesión.
- Navegación entre Productos, Usuarios y Ventas.
- Consulta de los usuarios registrados.
- Visualización y gestión de productos.
- Selección de un usuario registrado para realizar una venta.
- Selección de un producto registrado.
- Registro mediante el botón **Registrar venta**.
- Ejecución del callback mediante `command=`.
- Validación de la operación mediante `RestauranteServicio`.
- Actualización de la tabla después de registrar una venta.
- Almacenamiento de la venta en `ventas.json`.
- Cierre completo de la aplicación.
- Nueva ejecución para comprobar la persistencia de las ventas.
- Visualización del logo y los íconos almacenados en `assets`.

Estas pruebas me permitieron comprobar que las funciones desarrolladas anteriormente continúan trabajando y que la nueva sección de Ventas se encuentra integrada al sistema.

## Conclusión

Con esta actividad pude comprender de una manera más práctica cómo funciona el manejo básico de eventos en una interfaz gráfica.

Al presionar el botón **Registrar venta**, `command=` permite ejecutar un callback. Este callback obtiene la información seleccionada en la interfaz y solicita a `RestauranteServicio` que realice la operación. Después de registrar la venta, la información se guarda y la interfaz se actualiza para mostrar el resultado.

También pude continuar mejorando el mismo proyecto que he venido desarrollando durante las semanas anteriores. En esta semana incorporé la gestión de ventas, la persistencia mediante `ventas.json` y los recursos visuales de la carpeta `assets`, manteniendo separadas la interfaz, la lógica del sistema y el manejo de los datos.