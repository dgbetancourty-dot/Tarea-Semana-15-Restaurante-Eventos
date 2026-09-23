class Venta:
    def __init__(
        self,
        usuario,
        producto,
        fecha
    ):
        self.usuario = usuario
        self.producto = producto
        self.fecha = fecha

    def a_diccionario(self):
        return {
            "usuario": self.usuario,
            "producto": self.producto,
            "fecha": self.fecha
        }