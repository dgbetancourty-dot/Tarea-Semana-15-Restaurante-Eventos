class Producto:
    def __init__(
        self,
        codigo: str,
        nombre: str,
        precio: float,
        categoria: str,
        stock: int
    ) -> None:

        if not codigo.strip():
            raise ValueError("El código no puede estar vacío.")

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        if not categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")

        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        self._codigo = codigo.strip()
        self._nombre = nombre.strip()
        self._precio = precio
        self._categoria = categoria.strip()
        self._stock = stock

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        if not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        self._nombre = nuevo_nombre.strip()

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio: float) -> None:
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        self._precio = nuevo_precio

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, nueva_categoria: str) -> None:
        if not nueva_categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")

        self._categoria = nueva_categoria.strip()

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, nuevo_stock: int) -> None:
        if nuevo_stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        self._stock = nuevo_stock

    def vender(self, cantidad: int) -> bool:
        if cantidad <= 0:
            return False

        if cantidad > self._stock:
            return False

        self._stock -= cantidad
        return True

    def a_diccionario(self) -> dict:
        return {
            "codigo": self._codigo,
            "nombre": self._nombre,
            "precio": self._precio,
            "categoria": self._categoria,
            "stock": self._stock
        }

    def mostrar_informacion(self) -> None:
        print(f"Código: {self._codigo}")
        print(f"Nombre: {self._nombre}")
        print(f"Precio: ${self._precio:.2f}")
        print(f"Categoría: {self._categoria}")
        print(f"Stock: {self._stock}")