import tkinter as tk
from tkinter import messagebox, ttk
from pathlib import Path


RUTA_ASSETS = Path(__file__).parent.parent / "assets"


class MainView:
    def __init__(
        self,
        contenedor,
        restaurante_servicio,
        cerrar_sesion
    ):
        self.contenedor = contenedor
        self.restaurante_servicio = restaurante_servicio
        self.cerrar_sesion = cerrar_sesion

        # Recursos visuales de la aplicación
        self.logo_app = tk.PhotoImage(
            file=str(RUTA_ASSETS / "logo_app.png")
        )
        self.icono_productos = tk.PhotoImage(
            file=str(RUTA_ASSETS / "productos_icon.png")
        )
        self.icono_usuarios = tk.PhotoImage(
            file=str(RUTA_ASSETS / "usuarios_icon.png")
        )
        self.icono_ventas = tk.PhotoImage(
            file=str(RUTA_ASSETS / "ventas_icon.png")
        )

        self.frame = tk.Frame(
            self.contenedor,
            bg="#f2f4f7"
        )
        self.frame.pack(fill="both", expand=True)

        self.crear_encabezado()
        self.crear_zona_principal()
        self.mostrar_productos()

    def crear_encabezado(self):
        encabezado = tk.Frame(
            self.frame,
            bg="#1f4e78",
            height=90
        )
        encabezado.pack(fill="x")
        encabezado.pack_propagate(False)

        tk.Label(
            encabezado,
            image=self.logo_app,
            bg="#1f4e78"
        ).pack(side="left", padx=(18, 8), pady=3)

        titulo = tk.Label(
            encabezado,
            text="SISTEMA DE RESTAURANTE",
            font=("Arial", 20, "bold"),
            bg="#1f4e78",
            fg="white"
        )
        titulo.pack(side="left", padx=8, pady=18)

        boton_cerrar = tk.Button(
            encabezado,
            text="Cerrar sesión",
            command=self.cerrar_sesion,
            bg="#c0392b",
            fg="white",
            width=14
        )
        boton_cerrar.pack(
            side="right",
            padx=25,
            pady=18
        )

    def crear_zona_principal(self):
        cuerpo = tk.Frame(
            self.frame,
            bg="#f2f4f7"
        )
        cuerpo.pack(fill="both", expand=True)

        menu = tk.Frame(
            cuerpo,
            bg="#d9e6f2",
            width=180
        )
        menu.pack(side="left", fill="y")
        menu.pack_propagate(False)

        tk.Label(
            menu,
            text="MENÚ",
            font=("Arial", 14, "bold"),
            bg="#d9e6f2"
        ).pack(pady=25)

        tk.Button(
            menu,
            text="Productos",
            image=self.icono_productos,
            compound="left",
            width=150,
            anchor="w",
            command=self.mostrar_productos
        ).pack(pady=8)

        tk.Button(
            menu,
            text="Usuarios",
            image=self.icono_usuarios,
            compound="left",
            width=150,
            anchor="w",
            command=self.mostrar_usuarios
        ).pack(pady=8)

        tk.Button(
            menu,
            text="Ventas",
            image=self.icono_ventas,
            compound="left",
            width=150,
            anchor="w",
            command=self.mostrar_ventas
        ).pack(pady=8)

        self.frame_contenido = tk.Frame(
            cuerpo,
            bg="#f2f4f7"
        )
        self.frame_contenido.pack(
            side="right",
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

    def limpiar_contenido(self):
        for componente in self.frame_contenido.winfo_children():
            componente.destroy()

    def mostrar_productos(self):
        self.limpiar_contenido()

        tk.Label(
            self.frame_contenido,
            text="GESTIÓN DE PRODUCTOS",
            font=("Arial", 17, "bold"),
            bg="#f2f4f7",
            fg="#1f4e78"
        ).pack(pady=(0, 10))

        formulario = ttk.LabelFrame(
            self.frame_contenido,
            text="Datos del producto",
            padding=12
        )
        formulario.pack(fill="x", pady=5)

        ttk.Label(
            formulario,
            text="Código:"
        ).grid(
            row=0,
            column=0,
            padx=8,
            pady=7,
            sticky="w"
        )

        self.entrada_codigo = ttk.Entry(
            formulario,
            width=25
        )
        self.entrada_codigo.grid(
            row=0,
            column=1,
            padx=8,
            pady=7
        )

        ttk.Label(
            formulario,
            text="Nombre:"
        ).grid(
            row=0,
            column=2,
            padx=8,
            pady=7,
            sticky="w"
        )

        self.entrada_nombre = ttk.Entry(
            formulario,
            width=25
        )
        self.entrada_nombre.grid(
            row=0,
            column=3,
            padx=8,
            pady=7
        )

        ttk.Label(
            formulario,
            text="Precio:"
        ).grid(
            row=1,
            column=0,
            padx=8,
            pady=7,
            sticky="w"
        )

        self.entrada_precio = ttk.Entry(
            formulario,
            width=25
        )
        self.entrada_precio.grid(
            row=1,
            column=1,
            padx=8,
            pady=7
        )

        ttk.Label(
            formulario,
            text="Categoría:"
        ).grid(
            row=1,
            column=2,
            padx=8,
            pady=7,
            sticky="w"
        )

        self.combo_categoria = ttk.Combobox(
            formulario,
            values=[
                "Comida",
                "Bebida",
                "Postre",
                "Otro"
            ],
            state="readonly",
            width=22
        )
        self.combo_categoria.grid(
            row=1,
            column=3,
            padx=8,
            pady=7
        )

        ttk.Label(
            formulario,
            text="Stock:"
        ).grid(
            row=2,
            column=0,
            padx=8,
            pady=7,
            sticky="w"
        )

        self.entrada_stock = ttk.Entry(
            formulario,
            width=25
        )
        self.entrada_stock.grid(
            row=2,
            column=1,
            padx=8,
            pady=7
        )

        acciones = tk.Frame(
            self.frame_contenido,
            bg="#f2f4f7"
        )
        acciones.pack(fill="x", pady=10)

        tk.Button(
            acciones,
            text="Registrar",
            width=13,
            bg="#27ae60",
            fg="white",
            command=self.registrar_producto
        ).pack(side="left", padx=4)

        tk.Button(
            acciones,
            text="Cargar",
            width=13,
            bg="#2980b9",
            fg="white",
            command=self.cargar_producto
        ).pack(side="left", padx=4)

        tk.Button(
            acciones,
            text="Actualizar",
            width=13,
            bg="#f39c12",
            fg="white",
            command=self.actualizar_producto
        ).pack(side="left", padx=4)

        tk.Button(
            acciones,
            text="Eliminar",
            width=13,
            bg="#c0392b",
            fg="white",
            command=self.eliminar_producto
        ).pack(side="left", padx=4)

        tk.Button(
            acciones,
            text="Limpiar",
            width=13,
            command=self.limpiar_formulario
        ).pack(side="left", padx=4)

        listado = ttk.LabelFrame(
            self.frame_contenido,
            text="Productos registrados",
            padding=10
        )
        listado.pack(
            fill="both",
            expand=True,
            pady=5
        )

        columnas = (
            "codigo",
            "nombre",
            "precio",
            "categoria",
            "stock"
        )

        self.tabla_productos = ttk.Treeview(
            listado,
            columns=columnas,
            show="headings",
            height=12
        )

        self.tabla_productos.heading(
            "codigo",
            text="Código"
        )
        self.tabla_productos.heading(
            "nombre",
            text="Nombre"
        )
        self.tabla_productos.heading(
            "precio",
            text="Precio"
        )
        self.tabla_productos.heading(
            "categoria",
            text="Categoría"
        )
        self.tabla_productos.heading(
            "stock",
            text="Stock"
        )

        self.tabla_productos.column(
            "codigo",
            width=90,
            anchor="center"
        )
        self.tabla_productos.column(
            "nombre",
            width=190
        )
        self.tabla_productos.column(
            "precio",
            width=90,
            anchor="center"
        )
        self.tabla_productos.column(
            "categoria",
            width=120,
            anchor="center"
        )
        self.tabla_productos.column(
            "stock",
            width=80,
            anchor="center"
        )

        barra = ttk.Scrollbar(
            listado,
            orient="vertical",
            command=self.tabla_productos.yview
        )

        self.tabla_productos.configure(
            yscrollcommand=barra.set
        )

        self.tabla_productos.pack(
            side="left",
            fill="both",
            expand=True
        )
        barra.pack(side="right", fill="y")

        self.actualizar_tabla_productos()

    def obtener_datos_formulario(self):
        return (
            self.entrada_codigo.get().strip(),
            self.entrada_nombre.get().strip(),
            self.entrada_precio.get().strip(),
            self.combo_categoria.get().strip(),
            self.entrada_stock.get().strip()
        )

    def registrar_producto(self):
        datos = self.obtener_datos_formulario()

        try:
            self.restaurante_servicio.registrar_producto(
                *datos
            )

            self.actualizar_tabla_productos()
            self.limpiar_formulario()

            messagebox.showinfo(
                "Producto",
                "Producto registrado correctamente."
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def cargar_producto(self):
        codigo = self.entrada_codigo.get().strip()

        if not codigo:
            messagebox.showwarning(
                "Aviso",
                "Ingrese el código del producto."
            )
            return

        producto = (
            self.restaurante_servicio.buscar_producto(
                codigo
            )
        )

        if producto is None:
            messagebox.showerror(
                "Error",
                "No existe un producto con ese código."
            )
            return

        self.entrada_codigo.delete(0, tk.END)
        self.entrada_codigo.insert(
            0,
            producto.codigo
        )

        self.entrada_nombre.delete(0, tk.END)
        self.entrada_nombre.insert(
            0,
            producto.nombre
        )

        self.entrada_precio.delete(0, tk.END)
        self.entrada_precio.insert(
            0,
            str(producto.precio)
        )

        self.combo_categoria.set(
            producto.categoria
        )

        self.entrada_stock.delete(0, tk.END)
        self.entrada_stock.insert(
            0,
            str(producto.stock)
        )

        messagebox.showinfo(
            "Producto",
            "Producto cargado correctamente."
        )

    def actualizar_producto(self):
        datos = self.obtener_datos_formulario()

        try:
            self.restaurante_servicio.actualizar_producto(
                *datos
            )

            self.actualizar_tabla_productos()
            self.limpiar_formulario()

            messagebox.showinfo(
                "Producto",
                "Producto actualizado correctamente."
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def eliminar_producto(self):
        codigo = self.entrada_codigo.get().strip()

        if not codigo:
            messagebox.showwarning(
                "Aviso",
                "Ingrese el código del producto."
            )
            return

        confirmar = messagebox.askyesno(
            "Confirmar",
            "¿Desea eliminar este producto?"
        )

        if not confirmar:
            return

        try:
            self.restaurante_servicio.eliminar_producto(
                codigo
            )

            self.actualizar_tabla_productos()
            self.limpiar_formulario()

            messagebox.showinfo(
                "Producto",
                "Producto eliminado correctamente."
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def limpiar_formulario(self):
        self.entrada_codigo.delete(0, tk.END)
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_precio.delete(0, tk.END)
        self.combo_categoria.set("")
        self.entrada_stock.delete(0, tk.END)
        self.entrada_codigo.focus()

    def actualizar_tabla_productos(self):
        for fila in self.tabla_productos.get_children():
            self.tabla_productos.delete(fila)

        productos = (
            self.restaurante_servicio.listar_productos()
        )

        for producto in productos:
            self.tabla_productos.insert(
                "",
                tk.END,
                values=(
                    producto.codigo,
                    producto.nombre,
                    f"${producto.precio:.2f}",
                    producto.categoria,
                    producto.stock
                )
            )

    def mostrar_usuarios(self):
        self.limpiar_contenido()

        tk.Label(
            self.frame_contenido,
            text="USUARIOS REGISTRADOS",
            font=("Arial", 17, "bold"),
            bg="#f2f4f7",
            fg="#1f4e78"
        ).pack(pady=(0, 15))

        listado = ttk.LabelFrame(
            self.frame_contenido,
            text="Consulta de usuarios",
            padding=12
        )
        listado.pack(
            fill="both",
            expand=True
        )

        columnas = (
            "identificacion",
            "nombre",
            "correo"
        )

        tabla_usuarios = ttk.Treeview(
            listado,
            columns=columnas,
            show="headings"
        )

        tabla_usuarios.heading(
            "identificacion",
            text="Identificación"
        )
        tabla_usuarios.heading(
            "nombre",
            text="Nombre"
        )
        tabla_usuarios.heading(
            "correo",
            text="Correo"
        )

        tabla_usuarios.column(
            "identificacion",
            width=150,
            anchor="center"
        )
        tabla_usuarios.column(
            "nombre",
            width=220
        )
        tabla_usuarios.column(
            "correo",
            width=280
        )

        barra = ttk.Scrollbar(
            listado,
            orient="vertical",
            command=tabla_usuarios.yview
        )

        tabla_usuarios.configure(
            yscrollcommand=barra.set
        )

        tabla_usuarios.pack(
            side="left",
            fill="both",
            expand=True
        )
        barra.pack(side="right", fill="y")

        usuarios = (
            self.restaurante_servicio.listar_usuarios()
        )

        for usuario in usuarios:
            tabla_usuarios.insert(
                "",
                tk.END,
                values=(
                    usuario.identificacion,
                    usuario.nombre,
                    usuario.correo
                )
            )

    def mostrar_ventas(self):
        self.limpiar_contenido()

        tk.Label(
            self.frame_contenido,
            text="REGISTRO DE VENTAS",
            font=("Arial", 17, "bold"),
            bg="#f2f4f7",
            fg="#1f4e78"
        ).pack(pady=(0, 15))

        formulario = ttk.LabelFrame(
            self.frame_contenido,
            text="Datos de la venta",
            padding=12
        )
        formulario.pack(fill="x", pady=5)

        ttk.Label(
            formulario,
            text="Usuario:"
        ).grid(
            row=0,
            column=0,
            padx=8,
            pady=8,
            sticky="w"
        )

        usuarios = (
            self.restaurante_servicio.listar_usuarios()
        )

        self.usuarios_venta = {}

        for usuario in usuarios:
            texto = (
                f"{usuario.identificacion} - "
                f"{usuario.nombre}"
            )
            self.usuarios_venta[
                texto
            ] = usuario.identificacion

        self.combo_usuario_venta = ttk.Combobox(
            formulario,
            values=list(
                self.usuarios_venta.keys()
            ),
            state="readonly",
            width=35
        )
        self.combo_usuario_venta.grid(
            row=0,
            column=1,
            padx=8,
            pady=8
        )

        ttk.Label(
            formulario,
            text="Producto:"
        ).grid(
            row=1,
            column=0,
            padx=8,
            pady=8,
            sticky="w"
        )

        productos = (
            self.restaurante_servicio.listar_productos()
        )

        self.productos_venta = {}

        for producto in productos:
            texto = (
                f"{producto.codigo} - "
                f"{producto.nombre}"
            )
            self.productos_venta[
                texto
            ] = producto.codigo

        self.combo_producto_venta = ttk.Combobox(
            formulario,
            values=list(
                self.productos_venta.keys()
            ),
            state="readonly",
            width=35
        )
        self.combo_producto_venta.grid(
            row=1,
            column=1,
            padx=8,
            pady=8
        )

        tk.Button(
            formulario,
            text="Registrar venta",
            width=16,
            bg="#27ae60",
            fg="white",
            command=self.registrar_venta
        ).grid(
            row=2,
            column=0,
            columnspan=2,
            pady=12
        )

        listado = ttk.LabelFrame(
            self.frame_contenido,
            text="Ventas registradas",
            padding=10
        )
        listado.pack(
            fill="both",
            expand=True,
            pady=10
        )

        columnas = (
            "usuario",
            "producto",
            "fecha"
        )

        self.tabla_ventas = ttk.Treeview(
            listado,
            columns=columnas,
            show="headings",
            height=12
        )

        self.tabla_ventas.heading(
            "usuario",
            text="Usuario"
        )
        self.tabla_ventas.heading(
            "producto",
            text="Producto"
        )
        self.tabla_ventas.heading(
            "fecha",
            text="Fecha"
        )

        self.tabla_ventas.column(
            "usuario",
            width=200
        )
        self.tabla_ventas.column(
            "producto",
            width=220
        )
        self.tabla_ventas.column(
            "fecha",
            width=160,
            anchor="center"
        )

        barra = ttk.Scrollbar(
            listado,
            orient="vertical",
            command=self.tabla_ventas.yview
        )

        self.tabla_ventas.configure(
            yscrollcommand=barra.set
        )

        self.tabla_ventas.pack(
            side="left",
            fill="both",
            expand=True
        )
        barra.pack(
            side="right",
            fill="y"
        )

        self.actualizar_tabla_ventas()

    def registrar_venta(self):
        usuario_seleccionado = (
            self.combo_usuario_venta.get()
        )

        producto_seleccionado = (
            self.combo_producto_venta.get()
        )

        if not usuario_seleccionado:
            messagebox.showwarning(
                "Aviso",
                "Seleccione un usuario."
            )
            return

        if not producto_seleccionado:
            messagebox.showwarning(
                "Aviso",
                "Seleccione un producto."
            )
            return

        identificacion = self.usuarios_venta[
            usuario_seleccionado
        ]

        codigo_producto = self.productos_venta[
            producto_seleccionado
        ]

        try:
            self.restaurante_servicio.registrar_venta(
                identificacion,
                codigo_producto
            )

            self.actualizar_tabla_ventas()

            self.combo_usuario_venta.set("")
            self.combo_producto_venta.set("")

            messagebox.showinfo(
                "Venta",
                "Venta registrada correctamente."
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def actualizar_tabla_ventas(self):
        for fila in self.tabla_ventas.get_children():
            self.tabla_ventas.delete(fila)

        ventas = (
            self.restaurante_servicio.listar_ventas()
        )

        for venta in ventas:
            self.tabla_ventas.insert(
                "",
                tk.END,
                values=(
                    venta.usuario,
                    venta.producto,
                    venta.fecha
                )
            )

    def destruir(self):
        self.frame.destroy()