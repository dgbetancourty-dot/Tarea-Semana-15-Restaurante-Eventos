from datetime import datetime

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class RestauranteServicio:
    def __init__(
        self,
        productos_datos,
        usuarios_datos,
        ventas_datos,
        archivo_servicio
    ):
        self.archivo_servicio = archivo_servicio
        self.productos = []
        self.usuarios = []
        self.ventas = []

        self.cargar_productos(productos_datos)
        self.cargar_usuarios(usuarios_datos)
        self.cargar_ventas(ventas_datos)

    # ---------- CARGA DE DATOS ----------

    def cargar_productos(self, datos):
        for dato in datos:
            self.productos.append(
                Producto(
                    dato["codigo"],
                    dato["nombre"],
                    dato["precio"],
                    dato["categoria"],
                    dato["stock"]
                )
            )

    def cargar_usuarios(self, datos):
        for dato in datos:
            self.usuarios.append(
                Usuario(
                    dato["identificacion"],
                    dato["nombre"],
                    dato["correo"],
                    dato["contrasena"]
                )
            )

    def cargar_ventas(self, datos):
        for dato in datos:
            self.ventas.append(
                Venta(
                    dato["usuario"],
                    dato["producto"],
                    dato["fecha"]
                )
            )

    # ---------- ACCESO ----------

    def validar_acceso(self, usuario, contrasena):
        usuario_buscado = usuario.strip().lower()

        for registrado in self.usuarios:
            if (
                registrado.nombre.lower() == usuario_buscado
                and registrado.contrasena == contrasena
            ):
                return True

        return False

    # ---------- LISTADOS ----------

    def listar_productos(self):
        return self.productos

    def listar_usuarios(self):
        return self.usuarios

    def listar_ventas(self):
        return self.ventas

    # ---------- BÚSQUEDAS ----------

    def buscar_producto(self, codigo):
        codigo = codigo.strip().lower()

        for producto in self.productos:
            if producto.codigo.lower() == codigo:
                return producto

        return None

    def buscar_usuario(self, identificacion):
        identificacion = identificacion.strip()

        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                return usuario

        return None

    # ---------- PRODUCTOS ----------

    def registrar_producto(self, codigo, nombre, precio, categoria, stock):
        if self.buscar_producto(codigo):
            raise ValueError("Ya existe un producto con ese código.")

        precio = self._convertir_precio(precio)
        stock = self._convertir_stock(stock)

        producto = Producto(codigo, nombre, precio, categoria, stock)

        self.productos.append(producto)
        self.guardar_productos()

        return producto

    def actualizar_producto(self, codigo, nombre, precio, categoria, stock):
        producto = self.buscar_producto(codigo)

        if producto is None:
            raise ValueError("No existe un producto con ese código.")

        precio = self._convertir_precio(precio)
        stock = self._convertir_stock(stock)

        actualizado = Producto(
            producto.codigo,
            nombre,
            precio,
            categoria,
            stock
        )

        posicion = self.productos.index(producto)
        self.productos[posicion] = actualizado
        self.guardar_productos()

        return actualizado

    def eliminar_producto(self, codigo):
        producto = self.buscar_producto(codigo)

        if producto is None:
            raise ValueError("No existe un producto con ese código.")

        self.productos.remove(producto)
        self.guardar_productos()

    # ---------- VENTAS ----------

    def registrar_venta(self, identificacion_usuario, codigo_producto):
        usuario = self.buscar_usuario(identificacion_usuario)
        if usuario is None:
            raise ValueError("El usuario seleccionado no existe.")

        producto = self.buscar_producto(codigo_producto)
        if producto is None:
            raise ValueError("El producto seleccionado no existe.")

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
        venta = Venta(usuario.nombre, producto.nombre, fecha)

        self.ventas.append(venta)
        self.guardar_ventas()

        return venta

    # ---------- PERSISTENCIA ----------

    def guardar_productos(self):
        self.archivo_servicio.guardar_productos(self.productos)

    def guardar_ventas(self):
        self.archivo_servicio.guardar_ventas(self.ventas)

    # ---------- VALIDACIONES ----------

    @staticmethod
    def _convertir_precio(precio):
        try:
            return float(precio)
        except (ValueError, TypeError):
            raise ValueError("El precio debe ser un número válido.")

    @staticmethod
    def _convertir_stock(stock):
        try:
            return int(stock)
        except (ValueError, TypeError):
            raise ValueError("El stock debe ser un número entero.")
