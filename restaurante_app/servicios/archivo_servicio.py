import json
from pathlib import Path


class ArchivoServicio:
    def __init__(self, ruta_datos):
        self.ruta_datos = Path(ruta_datos)

    def cargar_json(self, nombre_archivo):
        ruta = self.ruta_datos / nombre_archivo

        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def guardar_json(self, nombre_archivo, datos):
        ruta = self.ruta_datos / nombre_archivo

        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)

    def cargar_productos(self):
        return self.cargar_json("productos.json")

    def cargar_usuarios(self):
        return self.cargar_json("usuarios.json")

    def cargar_ventas(self):
        return self.cargar_json("ventas.json")

    def guardar_productos(self, productos):
        datos = [producto.a_diccionario() for producto in productos]
        self.guardar_json("productos.json", datos)

    def guardar_ventas(self, ventas):
        datos = [venta.a_diccionario() for venta in ventas]
        self.guardar_json("ventas.json", datos)