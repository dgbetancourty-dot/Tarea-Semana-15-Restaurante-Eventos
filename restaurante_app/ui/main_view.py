import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk


RUTA_ASSETS = Path(__file__).parent.parent / "assets"

COLOR_FONDO = "#f2f4f7"
COLOR_TITULO = "#1f4e78"


class MainView:
    def __init__(self, contenedor, restaurante_servicio, cerrar_sesion):
        self.contenedor = contenedor
        self.restaurante_servicio = restaurante_servicio
        self.cerrar_sesion = cerrar_sesion

        # Recursos visuales (se guardan en atributos para que Tkinter
        # no los elimine de memoria)
        self.logo_app = self._cargar_imagen("logo_app.png")
        self.icono_productos = self._cargar_imagen("productos_icon.png")
        self.icono_usuarios = self._cargar_imagen("usuarios_icon.png")
        self.icono_ventas = self._cargar_imagen("ventas_icon.png")

        self.frame = tk.Frame(self.contenedor, bg=COLOR_FONDO)
        self.frame.pack(fill="both", expand=True)

        self.crear_encabezado()
        self.crear_zona_principal()
        self.mostrar_productos()

    @staticmethod
    def _cargar_imagen(nombre):
        return tk.PhotoImage(file=str(RUTA_ASSETS / nombre))

    # =========================================================
    # ESTRUCTURA PRINCIPAL
    # =========================================================

    def crear_encabezado(self):
        encabezado = tk.Frame(self.frame, bg=COLOR_TITULO, height=90)
        encabezado.pack(fill="x")
        encabezado.pack_propagate(False)

        tk.Label(
            encabezado,
            image=self.logo_app,
            bg=COLOR_TITULO
        ).pack(side="left", padx=(18, 8), pady=3)

        tk.Label(
            encabezado,
            text="SISTEMA DE RESTAURANTE",
            font=("Arial", 20, "bold"),
            bg=COLOR_TITULO,
            fg="white"
        ).pack(side="left", padx=8, pady=18)

        tk.Button(
            encabezado,
            text="Cerrar sesión",
            command=self.cerrar_sesion,
            bg="#c0392b",
            fg="white",
            width=14
        ).pack(side="right", padx=25, pady=18)

    def crear_zona_principal(self):
        cuerpo = tk.Frame(self.frame, bg=COLOR_FONDO)
        cuerpo.pack(fill="both", expand=True)

        menu = tk.Frame(cuerpo, bg="#d9e6f2", width=180)
        menu.pack(side="left", fill="y")
        menu.pack_propagate(False)

        tk.Label(
            menu,
            text="MENÚ",
            font=("Arial", 14, "bold"),
            bg="#d9e6f2"
        ).pack(pady=25)

        opciones = [
            ("Productos", self.icono_productos, self.mostrar_productos),
            ("Usuarios", self.icono_usuarios, self.mostrar_usuarios),
            ("Ventas", self.icono_ventas, self.mostrar_ventas)
        ]

        for texto, icono, comando in opciones:
            tk.Button(
                menu,
                text=texto,
                image=icono,
                compound="left",
                width=150,
                anchor="w",
                command=comando
            ).pack(pady=8)

        self.frame_contenido = tk.Frame(cuerpo, bg=COLOR_FONDO)
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

    def crear_titulo(self, texto, espacio=10):
        tk.Label(
            self.frame_contenido,
            text=texto,
            font=("Arial", 17, "bold"),
            bg=COLOR_FONDO,
            fg=COLOR_TITULO
        ).pack(pady=(0, espacio))

    def crear_tabla(self, titulo, columnas, altura=12):
        """Crea un Treeview con barra de desplazamiento.

        columnas: lista de (clave, encabezado, ancho, alineación).
        """
        listado = ttk.LabelFrame(
            self.frame_contenido,
            text=titulo,
            padding=10
        )
        listado.pack(fill="both", expand=True, pady=5)

        tabla = ttk.Treeview(
            listado,
            columns=[clave for clave, *_ in columnas],
            show="headings",
            height=altura
        )

        for clave, encabezado, ancho, alineacion in columnas:
            tabla.heading(clave, text=encabezado)
            tabla.column(clave, width=ancho, anchor=alineacion)

        barra = ttk.Scrollbar(
            listado,
            orient="vertical",
            command=tabla.yview
        )
        tabla.configure(yscrollcommand=barra.set)

        tabla.pack(side="left", fill="both", expand=True)
        barra.pack(side="right", fill="y")

        return tabla

    @staticmethod
    def llenar_tabla(tabla, filas):
        tabla.delete(*tabla.get_children())

        for fila in filas:
            tabla.insert("", tk.END, values=fila)

    # =========================================================
    # PRODUCTOS
    # =========================================================

    def mostrar_productos(self):
        self.limpiar_contenido()
        self.crear_titulo("GESTIÓN DE PRODUCTOS")

        formulario = ttk.LabelFrame(
            self.frame_contenido,
            text="Datos del producto",
            padding=12
        )
        formulario.pack(fill="x", pady=5)

        def etiqueta(texto, fila, columna):
            ttk.Label(formulario, text=texto).grid(
                row=fila, column=columna, padx=8, pady=7, sticky="w"
            )

        etiqueta("Código:", 0, 0)
        self.entrada_codigo = ttk.Entry(formulario, width=25)
        self.entrada_codigo.grid(row=0, column=1, padx=8, pady=7)

        etiqueta("Nombre:", 0, 2)
        self.entrada_nombre = ttk.Entry(formulario, width=25)
        self.entrada_nombre.grid(row=0, column=3, padx=8, pady=7)

        etiqueta("Precio:", 1, 0)
        self.entrada_precio = ttk.Entry(formulario, width=25)
        self.entrada_precio.grid(row=1, column=1, padx=8, pady=7)

        etiqueta("Categoría:", 1, 2)
        self.combo_categoria = ttk.Combobox(
            formulario,
            values=["Comida", "Bebida", "Postre", "Otro"],
            state="readonly",
            width=22
        )
        self.combo_categoria.grid(row=1, column=3, padx=8, pady=7)

        etiqueta("Stock:", 2, 0)
        self.entrada_stock = ttk.Entry(formulario, width=25)
        self.entrada_stock.grid(row=2, column=1, padx=8, pady=7)

        acciones = tk.Frame(self.frame_contenido, bg=COLOR_FONDO)
        acciones.pack(fill="x", pady=10)

        botones = [
            ("Registrar", "#27ae60", self.registrar_producto),
            ("Cargar", "#2980b9", self.cargar_producto),
            ("Actualizar", "#f39c12", self.actualizar_producto),
            ("Eliminar", "#c0392b", self.eliminar_producto)
        ]

        for texto, color, comando in botones:
            tk.Button(
                acciones,
                text=texto,
                width=13,
                bg=color,
                fg="white",
                command=comando
            ).pack(side="left", padx=4)

        tk.Button(
            acciones,
            text="Limpiar",
            width=13,
            command=self.limpiar_formulario
        ).pack(side="left", padx=4)

        self.tabla_productos = self.crear_tabla(
            "Productos registrados",
            [
                ("codigo", "Código", 90, "center"),
                ("nombre", "Nombre", 190, "w"),
                ("precio", "Precio", 90, "center"),
                ("categoria", "Categoría", 120, "center"),
                ("stock", "Stock", 80, "center")
            ]
        )

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
        try:
            self.restaurante_servicio.registrar_producto(
                *self.obtener_datos_formulario()
            )
        except ValueError as error:
            messagebox.showerror("Error", str(error))
            return

        self.actualizar_tabla_productos()
        self.limpiar_formulario()
        messagebox.showinfo("Producto", "Producto registrado correctamente.")

    def cargar_producto(self):
        codigo = self.entrada_codigo.get().strip()

        if not codigo:
            messagebox.showwarning("Aviso", "Ingrese el código del producto.")
            return

        producto = self.restaurante_servicio.buscar_producto(codigo)

        if producto is None:
            messagebox.showerror(
                "Error",
                "No existe un producto con ese código."
            )
            return

        self.limpiar_formulario()

        self.entrada_codigo.insert(0, producto.codigo)
        self.entrada_nombre.insert(0, producto.nombre)
        self.entrada_precio.insert(0, str(producto.precio))
        self.combo_categoria.set(producto.categoria)
        self.entrada_stock.insert(0, str(producto.stock))

        messagebox.showinfo("Producto", "Producto cargado correctamente.")

    def actualizar_producto(self):
        try:
            self.restaurante_servicio.actualizar_producto(
                *self.obtener_datos_formulario()
            )
        except ValueError as error:
            messagebox.showerror("Error", str(error))
            return

        self.actualizar_tabla_productos()
        self.limpiar_formulario()
        messagebox.showinfo("Producto", "Producto actualizado correctamente.")

    def eliminar_producto(self):
        codigo = self.entrada_codigo.get().strip()

        if not codigo:
            messagebox.showwarning("Aviso", "Ingrese el código del producto.")
            return

        if not messagebox.askyesno("Confirmar", "¿Desea eliminar este producto?"):
            return

        try:
            self.restaurante_servicio.eliminar_producto(codigo)
        except ValueError as error:
            messagebox.showerror("Error", str(error))
            return

        self.actualizar_tabla_productos()
        self.limpiar_formulario()
        messagebox.showinfo("Producto", "Producto eliminado correctamente.")

    def limpiar_formulario(self):
        self.entrada_codigo.delete(0, tk.END)
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_precio.delete(0, tk.END)
        self.combo_categoria.set("")
        self.entrada_stock.delete(0, tk.END)
        self.entrada_codigo.focus()

    def actualizar_tabla_productos(self):
        self.llenar_tabla(
            self.tabla_productos,
            [
                (
                    producto.codigo,
                    producto.nombre,
                    f"${producto.precio:.2f}",
                    producto.categoria,
                    producto.stock
                )
                for producto in self.restaurante_servicio.listar_productos()
            ]
        )

    # =========================================================
    # USUARIOS
    # =========================================================

    def mostrar_usuarios(self):
        self.limpiar_contenido()
        self.crear_titulo("USUARIOS REGISTRADOS", espacio=15)

        tabla_usuarios = self.crear_tabla(
            "Consulta de usuarios",
            [
                ("identificacion", "Identificación", 150, "center"),
                ("nombre", "Nombre", 220, "w"),
                ("correo", "Correo", 280, "w")
            ]
        )

        self.llenar_tabla(
            tabla_usuarios,
            [
                (usuario.identificacion, usuario.nombre, usuario.correo)
                for usuario in self.restaurante_servicio.listar_usuarios()
            ]
        )

    # =========================================================
    # VENTAS
    # =========================================================

    def mostrar_ventas(self):
        self.limpiar_contenido()
        self.crear_titulo("REGISTRO DE VENTAS", espacio=15)

        formulario = ttk.LabelFrame(
            self.frame_contenido,
            text="Datos de la venta",
            padding=12
        )
        formulario.pack(fill="x", pady=5)

        # Texto mostrado en el combobox -> identificador que usa el servicio
        self.usuarios_venta = {
            f"{usuario.identificacion} - {usuario.nombre}":
                usuario.identificacion
            for usuario in self.restaurante_servicio.listar_usuarios()
        }
        self.productos_venta = {
            f"{producto.codigo} - {producto.nombre}": producto.codigo
            for producto in self.restaurante_servicio.listar_productos()
        }

        ttk.Label(formulario, text="Usuario:").grid(
            row=0, column=0, padx=8, pady=8, sticky="w"
        )
        self.combo_usuario_venta = ttk.Combobox(
            formulario,
            values=list(self.usuarios_venta),
            state="readonly",
            width=35
        )
        self.combo_usuario_venta.grid(row=0, column=1, padx=8, pady=8)

        ttk.Label(formulario, text="Producto:").grid(
            row=1, column=0, padx=8, pady=8, sticky="w"
        )
        self.combo_producto_venta = ttk.Combobox(
            formulario,
            values=list(self.productos_venta),
            state="readonly",
            width=35
        )
        self.combo_producto_venta.grid(row=1, column=1, padx=8, pady=8)

        # command= recibe el callback SIN paréntesis: se ejecuta al pulsar
        tk.Button(
            formulario,
            text="Registrar venta",
            width=16,
            bg="#27ae60",
            fg="white",
            command=self.registrar_venta
        ).grid(row=2, column=0, columnspan=2, pady=12)

        self.tabla_ventas = self.crear_tabla(
            "Ventas registradas",
            [
                ("usuario", "Usuario", 200, "w"),
                ("producto", "Producto", 220, "w"),
                ("fecha", "Fecha", 160, "center")
            ]
        )

        self.actualizar_tabla_ventas()

    def registrar_venta(self):
        """Callback del botón 'Registrar venta'.

        Obtiene las selecciones de la interfaz, delega la validación y el
        registro en RestauranteServicio y actualiza la vista.
        """
        usuario_seleccionado = self.combo_usuario_venta.get()
        producto_seleccionado = self.combo_producto_venta.get()

        if not usuario_seleccionado:
            messagebox.showwarning("Aviso", "Seleccione un usuario.")
            return

        if not producto_seleccionado:
            messagebox.showwarning("Aviso", "Seleccione un producto.")
            return

        try:
            self.restaurante_servicio.registrar_venta(
                self.usuarios_venta[usuario_seleccionado],
                self.productos_venta[producto_seleccionado]
            )
        except ValueError as error:
            messagebox.showerror("Error", str(error))
            return

        self.actualizar_tabla_ventas()

        self.combo_usuario_venta.set("")
        self.combo_producto_venta.set("")

        messagebox.showinfo("Venta", "Venta registrada correctamente.")

    def actualizar_tabla_ventas(self):
        self.llenar_tabla(
            self.tabla_ventas,
            [
                (venta.usuario, venta.producto, venta.fecha)
                for venta in self.restaurante_servicio.listar_ventas()
            ]
        )

    # =========================================================
    # CIERRE DE VISTA
    # =========================================================

    def destruir(self):
        self.frame.destroy()
