import tkinter as tk
from pathlib import Path
from tkinter import messagebox


RUTA_ASSETS = Path(__file__).parent.parent / "assets"


class LoginView:
    def __init__(self, contenedor, restaurante_servicio, mostrar_main):
        self.contenedor = contenedor
        self.restaurante_servicio = restaurante_servicio
        self.mostrar_main = mostrar_main

        self.logo = tk.PhotoImage(file=str(RUTA_ASSETS / "logo_app.png"))

        self.frame = tk.Frame(self.contenedor, bg="#f2f4f7")
        self.frame.pack(fill="both", expand=True)

        encabezado = tk.Frame(self.frame, bg="#1f4e78", height=90)
        encabezado.pack(fill="x")
        encabezado.pack_propagate(False)

        tk.Label(
            encabezado,
            text="SISTEMA DE RESTAURANTE",
            font=("Arial", 20, "bold"),
            bg="#1f4e78",
            fg="white"
        ).pack(pady=28)

        tk.Label(self.frame, image=self.logo, bg="#f2f4f7").pack(pady=(25, 5))

        tk.Label(
            self.frame,
            text="ACCESO AL RESTAURANTE",
            font=("Arial", 17, "bold"),
            bg="#f2f4f7",
            fg="#1f4e78"
        ).pack(pady=(5, 15))

        self.entrada_usuario = self._crear_campo("Usuario o nombre:")
        self.entrada_contrasena = self._crear_campo("Contraseña:", oculto=True)

        tk.Button(
            self.frame,
            text="Ingresar",
            width=20,
            bg="#27ae60",
            fg="white",
            command=self.validar_acceso
        ).pack(pady=20)

    def _crear_campo(self, texto, oculto=False):
        tk.Label(self.frame, text=texto, bg="#f2f4f7").pack()

        entrada = tk.Entry(self.frame, width=30, show="*" if oculto else "")
        entrada.pack(pady=8)

        return entrada

    def validar_acceso(self):
        usuario = self.entrada_usuario.get().strip()
        contrasena = self.entrada_contrasena.get().strip()

        if not usuario or not contrasena:
            messagebox.showwarning(
                "Aviso",
                "Complete usuario o nombre y contraseña."
            )
            return

        if self.restaurante_servicio.validar_acceso(usuario, contrasena):
            messagebox.showinfo("Acceso", "Ingreso correcto.")
            self.mostrar_main()
        else:
            messagebox.showerror(
                "Error",
                "Usuario, nombre o contraseña incorrectos."
            )

    def destruir(self):
        self.frame.destroy()
