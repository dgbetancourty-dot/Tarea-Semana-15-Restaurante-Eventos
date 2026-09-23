class Usuario:
    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str
    ) -> None:

        if not identificacion.strip():
            raise ValueError(
                "La identificación no puede estar vacía."
            )

        if not nombre.strip():
            raise ValueError(
                "El nombre no puede estar vacío."
            )

        if not correo.strip():
            raise ValueError(
                "El correo no puede estar vacío."
            )

        if "@" not in correo:
            raise ValueError(
                "El correo electrónico no es válido."
            )

        self._identificacion = identificacion.strip()
        self._nombre = nombre.strip()
        self._correo = correo.strip()

    @property
    def identificacion(self) -> str:
        return self._identificacion

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def correo(self) -> str:
        return self._correo

    def a_diccionario(self) -> dict:
        return {
            "identificacion": self._identificacion,
            "nombre": self._nombre,
            "correo": self._correo
        }

    def mostrar_informacion(self) -> None:
        print(
            f"Identificación: {self._identificacion}"
        )
        print(f"Nombre: {self._nombre}")
        print(f"Correo: {self._correo}")