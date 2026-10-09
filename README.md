# Sistema de Restaurante - Semana 15: Manejo de eventos con Tkinter

## Descripción

En esta actividad continué desarrollando mi Sistema de Restaurante utilizando Python y Tkinter. El objetivo principal fue aplicar el manejo básico de eventos en una interfaz gráfica mediante botones y funciones callback.

Para realizar la práctica incorporé una sección de Ventas, donde se puede seleccionar un usuario y un producto que ya estén registrados y guardar la venta al presionar un botón.

Mantuve la organización del proyecto en módulos, el inicio de sesión, la gestión de productos, la consulta de usuarios y el almacenamiento de información mediante archivos JSON.

## Funcionalidades del sistema

### Productos

- Registrar nuevos productos.
- Consultar productos existentes.
- Actualizar la información de los productos.
- Eliminar productos registrados.
- Visualizar los productos en una tabla.

### Usuarios

- Consultar los usuarios registrados.
- Visualizar la identificación, el nombre y el correo electrónico de cada usuario.

### Ventas

- Seleccionar un usuario registrado.
- Seleccionar un producto existente.
- Registrar una venta mediante un botón.
- Guardar el usuario, el producto y la fecha del registro.
- Mostrar las ventas en una tabla.
- Actualizar la tabla después de registrar una venta.
- Conservar los registros al cerrar y volver a abrir el programa.

## Estructura del proyecto

El sistema está organizado en carpetas para separar las diferentes responsabilidades de la aplicación.

```text
restaurante_app/
├── assets/
│   ├── logo.png
│   ├── logo_app.png
│   ├── productos.png
│   ├── productos_icon.png
│   ├── usuarios.png
│   ├── usuarios_icon.png
│   ├── ventas.png
│   └── ventas_icon.png
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
└── main.py
```

Las carpetas cumplen las siguientes funciones:

- **modelos:** contiene las clases `Producto`, `Usuario` y `Venta`.
- **servicios:** contiene las operaciones del sistema y los métodos para trabajar con los archivos JSON.
- **ui:** contiene las ventanas y los componentes gráficos desarrollados con Tkinter.
- **datos:** almacena la información de productos, usuarios y ventas.
- **assets:** contiene el logotipo y los íconos utilizados en la aplicación.
- **main.py:** es el archivo principal desde el cual se ejecuta el sistema.

Esta organización me permitió incorporar el registro de ventas sin tener que desarrollar nuevamente toda la aplicación.

## Registro de ventas

La nueva sección de Ventas permite seleccionar un usuario y un producto que ya se encuentren registrados en el sistema.

Para realizar una venta, primero se selecciona el usuario y después el producto mediante listas desplegables. Al presionar el botón **Registrar venta**, la aplicación comprueba los datos y guarda el registro.

Cada venta contiene:

- Nombre del usuario.
- Nombre del producto.
- Fecha y hora del registro.

Después de registrar la venta, la tabla se actualiza para mostrar la información ingresada.

## Manejo de eventos con Tkinter

Para aplicar el tema estudiado utilicé la propiedad `command` de Tkinter, que permite relacionar un botón con una función.

En el botón **Registrar venta** se utiliza la siguiente instrucción:

```python
command=self.registrar_venta
```

Cuando el usuario presiona el botón, se ejecuta el método `registrar_venta`, que funciona como callback.

Este método obtiene el usuario y el producto seleccionados y llama a `RestauranteServicio` para realizar la operación.

El proceso funciona de la siguiente manera:

1. El usuario selecciona un usuario y un producto.
2. Presiona el botón **Registrar venta**.
3. Tkinter ejecuta el callback `registrar_venta`.
4. El callback envía los datos a `RestauranteServicio`.
5. El servicio comprueba que el usuario y el producto existan.
6. Se registra la venta y se guarda en `ventas.json`.
7. La tabla se actualiza y aparece un mensaje de confirmación.

De esta manera pude comprender cómo una acción realizada en la interfaz puede ejecutar una función y actualizar la información del programa.

## Persistencia de datos

Para almacenar la información utilicé archivos JSON:

- `productos.json`: contiene los productos registrados.
- `usuarios.json`: contiene los usuarios del sistema.
- `ventas.json`: contiene las ventas realizadas.

La clase `ArchivoServicio` se encarga de leer y guardar los archivos JSON.

La interfaz no modifica directamente estos archivos, sino que utiliza los servicios del sistema.

Una vez registrada una venta, la información permanece guardada aunque se cierre el programa. Al volver a ejecutarlo, las ventas anteriores aparecen nuevamente en la tabla.

## Interfaz gráfica y recursos visuales

La aplicación utiliza Tkinter y componentes `ttk` para mostrar formularios, botones, listas desplegables y tablas.

El menú principal permite ingresar a las secciones de Productos, Usuarios y Ventas.

También se utilizan recursos gráficos almacenados en la carpeta `assets`, entre ellos:

- Logotipo del Sistema de Restaurante.
- Ícono de Productos.
- Ícono de Usuarios.
- Ícono de Ventas.

Estos recursos ayudan a identificar las diferentes secciones y a mantener una presentación ordenada.

## Requisitos para ejecutar el programa

- Tener instalado Python 3.
- Contar con Tkinter, que normalmente viene incluido en Python para Windows.

El proyecto no necesita instalar bibliotecas externas para sus funciones principales.

## Ejecución del programa

Primero se debe abrir una terminal en la carpeta principal del repositorio.

Desde esa ubicación se puede ejecutar:

```powershell
python restaurante_app/main.py
```

Otra opción es ingresar a la carpeta de la aplicación:

```powershell
cd restaurante_app
python main.py
```

Al ejecutar el programa se abrirá la pantalla de inicio de sesión.

## Acceso de prueba

Para facilitar la revisión del proyecto, se pueden utilizar las siguientes credenciales de demostración:

**Usuario:** Dennis

**Contraseña:** 1234

Estas credenciales son únicamente para probar el funcionamiento de esta actividad y no deben utilizarse como datos de acceso reales.

Después de iniciar sesión se puede acceder a las secciones de Productos, Usuarios y Ventas.

## Pruebas de funcionamiento

Durante la revisión del proyecto realicé las siguientes comprobaciones:

- Ejecuté el programa y comprobé que la ventana principal se abriera correctamente.
- Ingresé utilizando las credenciales de prueba.
- Accedí a la sección de Ventas.
- Seleccioné un usuario y un producto existentes.
- Registré una venta mediante el botón correspondiente.
- Comprobé que la venta apareciera en la tabla.
- Cerré completamente el programa y volví a ejecutarlo.
- Verifiqué que la venta registrada continuara almacenada y apareciera nuevamente.

Estas pruebas me permitieron comprobar el funcionamiento del registro de ventas y su almacenamiento en archivos JSON.

## Conclusión

Con esta actividad pude comprender mejor el manejo de eventos en Tkinter y la importancia de utilizar funciones callback para responder a las acciones del usuario.

La incorporación de la sección de Ventas me permitió relacionar los componentes gráficos con los servicios del sistema, registrar información y actualizar una tabla después de realizar una operación.

También reforcé mis conocimientos sobre programación orientada a objetos, organización modular y persistencia de datos mediante archivos JSON.

Considero que esta práctica fue útil porque me permitió aplicar lo aprendido en una aplicación funcional y seguir mejorando la estructura de mi proyecto.