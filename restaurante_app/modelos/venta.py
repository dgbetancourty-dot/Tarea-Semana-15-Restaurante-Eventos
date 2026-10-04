class Venta:
    """Relaciona un usuario con un producto en una fecha determinada."""

    def __init__(self, usuario: str, producto: str, fecha: str) -> None:
        if not usuario.strip():
            raise ValueError("El usuario de la venta no puede estar vacío.")

        if not producto.strip():
            raise ValueError("El producto de la venta no puede estar vacío.")

        if not fecha.strip():
            raise ValueError("La fecha de la venta no puede estar vacía.")

        self._usuario = usuario.strip()
        self._producto = producto.strip()
        self._fecha = fecha.strip()

    @property
    def usuario(self) -> str:
        return self._usuario

    @property
    def producto(self) -> str:
        return self._producto

    @property
    def fecha(self) -> str:
        return self._fecha

    def a_diccionario(self) -> dict:
        return {
            "usuario": self._usuario,
            "producto": self._producto,
            "fecha": self._fecha
        }
