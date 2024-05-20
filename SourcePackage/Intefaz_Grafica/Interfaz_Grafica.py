import os.path
import tkinter as tk
from tkinter import ttk, messagebox
from SourcePackage.Validacion.Validador import Validador
from SourcePackage.Gestor_Licencia.Gestor_Licencia import Gestor_Licencia


class Interfaz_Grafica:
    def __init__(self, master, gestor):
        self.master = master
        self.gestor = gestor
        self.configurar_ventana()
        self.configurar_estilos()
        self.crear_widgets()
        self.ventana_activacion = None
        self.llave_almacenada = self.gestor.cargar_llave_almacenada()

    def configurar_ventana(self):
        """
            Configura la ventana principal del formulario de registro.

            Establece el título, el color de fondo, el tamaño mínimo y la configuración de redimensionamiento.
            """
        self.master.title("Formulario de registro")
        self.master.configure(background='white')
        self.master.minsize(width=700, height=540)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

    def configurar_estilos(self):
        # Configurar el estilo para los widgets ttk
        style = ttk.Style()
        style.configure('TFrame', background='white')
        style.configure('TLabel', background='white', foreground='black')
        style.configure('TEntry', fieldbackground='white', foreground='black')
        style.configure("Hover.TButton", background="lightgrey")

    def crear_widgets(self):
        self.crear_frame_principal()
        self.crear_campo_entrada()
        self.crear_botones()
        self.crear_imagen()

    def crear_frame_principal(self):
        # Crear un frame principal que se expanda con la ventana
        self.main_frame = ttk.Frame(self.master, style='TFrame')
        self.main_frame.grid(sticky='nsew')
        # Configurar el redimensionamiento del frame principal
        self.main_frame.columnconfigure(0, weight=1)
        for i in range(9):  # Asumiendo que tienes 8 filas
            self.main_frame.rowconfigure(i, weight=1)

    def crear_campo_entrada(self):
        # Etiquetas y campos de entrada
        nombre = ttk.Label(self.main_frame, text="Nombre:")
        nombre.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.entrada_nombre = ttk.Entry(self.main_frame)
        self.entrada_nombre.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

        self.entrada_nombre.bind("<Enter>", lambda e: self._mostrar_tooltip(e, "Ingrese su primer nombre"))
        self.entrada_nombre.bind("<Leave>", lambda e: self._ocultar_tooltip())

        apellido = ttk.Label(self.main_frame, text="Primer Apellido:")
        apellido.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        self.entrada_apellido = ttk.Entry(self.main_frame)
        self.entrada_apellido.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)

        self.entrada_apellido.bind("<Enter>", lambda e: self._mostrar_tooltip(e, "Ingrese su primer apellido"))
        self.entrada_apellido.bind("<Leave>", lambda e: self._ocultar_tooltip())

        telefono = ttk.Label(self.main_frame, text="Teléfono:")
        telefono.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        self.entrada_telefono = ttk.Entry(self.main_frame)
        self.entrada_telefono.grid(column=1, row=3, sticky=tk.EW, padx=5, pady=5)

        centro_trabajo = ttk.Label(self.main_frame, text="Centro de Trabajo:")
        centro_trabajo.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
        self.entrada_centro_trabajo = ttk.Entry(self.main_frame)
        self.entrada_centro_trabajo.grid(column=1, row=4, sticky=tk.EW, padx=5, pady=5)

        cargo = ttk.Label(self.main_frame, text="Cargo:")
        cargo.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        self.entrada_cargo = ttk.Entry(self.main_frame)
        self.entrada_cargo.grid(column=1, row=5, sticky=tk.EW, padx=5, pady=5)

        usuario = ttk.Label(self.main_frame, text="Nombre de Usuario:")
        usuario.grid(column=0, row=6, sticky=tk.W, padx=5, pady=5)
        self.entrada_usuario = ttk.Entry(self.main_frame)
        self.entrada_usuario.grid(column=1, row=6, sticky=tk.EW, padx=5, pady=5)

        email = ttk.Label(self.main_frame, text="Correo Electrónico:")
        email.grid(column=0, row=7, sticky=tk.W, padx=5, pady=5)
        self.entrada_email = ttk.Entry(self.main_frame)
        self.entrada_email.grid(column=1, row=7, sticky=tk.EW, padx=5, pady=5)

        self.entrada_email.bind("<Enter>", lambda e: self._mostrar_tooltip(e, "Formato: usuario.@dominio.com"))
        self.entrada_email.bind("<Leave>", lambda e: self._ocultar_tooltip())

        contrasenia = ttk.Label(self.main_frame, text="Contraseña:")
        contrasenia.grid(column=0, row=8, sticky=tk.W, padx=5, pady=5)
        self.entrada_contrasenia = ttk.Entry(self.main_frame, show="*")
        self.entrada_contrasenia.grid(column=1, row=8, sticky=tk.EW, padx=5, pady=5)

        self.entrada_contrasenia.bind("<Enter>", lambda e: self._mostrar_tooltip(e, "La contraseña debe contener numeros,"                                                                           " letras y caracteres especiales"))
        self.entrada_contrasenia.bind("<Leave>", lambda e: self._ocultar_tooltip())

    def crear_botones(self):
        # Boton para mostrar/ocultar la contraseña
        self.boton_mostrar = ttk.Button(self.main_frame, text="Mostrar", command=self.mostrar_contrasenia)
        self.boton_mostrar.grid(column=2, row=8, sticky=tk.W, padx=5, pady=5)
        # Botón para enviar el formulario
        self.iniciar_sesion = ttk.Button(self.main_frame, text="Iniciar sesion", command=self.proceso_iniciar_sesion)
        self.iniciar_sesion.grid(column=1, row=9, sticky=tk.EW, padx=5, pady=5)
        self.iniciar_sesion.bind("<Enter>", lambda e: self.on_enter(e))
        self.iniciar_sesion.bind("<Leave>", lambda e: self.on_leave(e))

        self.registrarse = ttk.Button(self.main_frame, text="Registrarse", command=self.registrar)
        self.registrarse.grid(column=0, row=9, sticky=tk.EW, padx=5, pady=5)
        self.registrarse.bind("<Enter>", lambda e: self.on_enter)
        self.registrarse.bind("<Leave>", lambda e: self.on_leave)

        # Botón para cerrar la ventana
        self.boton_cerrar = ttk.Button(self.main_frame, text="Cerrar", command=self.cerrar_ventana)
        self.boton_cerrar.grid(column=2, row=9, columnspan=2, sticky=tk.EW, padx=5, pady=5)

    def cerrar_ventana(self):
        # Cerrar la ventana actual
        self.master.destroy()

    def crear_imagen(self, contenedor=None):
        if contenedor is None:
            contenedor = self.main_frame

        directorio_actual = os.path.dirname(__file__)
        ruta_imagen = os.path.join(directorio_actual, 'Captura.PNG')
        try:
            # Cargar la imagen
            imagen = tk.PhotoImage(file=ruta_imagen)
            # Crear un widget de etiqueta para mostrar la imagen
            etiqueta_imagen = ttk.Label(contenedor, image=imagen)
            etiqueta_imagen.image = imagen
            etiqueta_imagen.grid(column=0, row=0, columnspan=3, sticky=tk.N, padx=5, pady=5)

            # Configurar el redimensionamiento de la imagen
            contenedor.rowconfigure(0, weight=1)
            contenedor.columnconfigure(0, weight=1)
            contenedor.columnconfigure(1, weight=1)
            contenedor.columnconfigure(2, weight=1)
        except tk.TclError as e:
            messagebox.showerror("Error al cargar la imagen", f"No se pudo cargar la imagen: {e}")

    def mostrar_contrasenia(self):
        """
            Alterna la visibilidad del campo de entrada de la contraseña.

            Si la contraseña está oculta, la muestra; si está visible, la oculta.
            """
        if self.entrada_contrasenia.cget('show') == '*':
            self.entrada_contrasenia.config(show='')
        else:
            self.entrada_contrasenia.config(show='*')

        self.master.columnconfigure(0, weight=1)

    def _mostrar_tooltip(self, event, texto):
        x, y, cx, cy = event.widget.bbox("insert")
        x += event.widget.winfo_rootx() + 25
        y += event.widget.winfo_rooty() + 20

        self.tooltip = tk.Toplevel(self.master)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry('+%d+%d' % (x, y))

        label = tk.Label(self.tooltip, text=texto, justify="left", background="white", relief="solid",
                         borderwidth=1, font=("arial", 10, "normal"))
        label.pack(ipadx=1)

    def _ocultar_tooltip(self):
        if self.tooltip:
            self.tooltip.destroy()

    def _mostrar_mensaje_archivo_usuario(self, existe_archivo):
        if existe_archivo:
            self.mostrar_mensaje_error("No se puede iniciar sesión sin un archivo de usuario. Por favor, regístrese primero.")
        else:
            self.mostrar_mensaje_error("No hay archivo de usuario disponible. Regístrese para crear uno.")

    def verificar_archivo_usuario(self):
        # Verificar si el archivo de datos del usuario existe
        existe_archivo = os.path.exists(self.gestor.archivo_usuario)
        self.iniciar_sesion.config(state=tk.NORMAL if existe_archivo else tk.DISABLED)
        self._mostrar_mensaje_archivo_usuario(existe_archivo)

    def mostrar_mensaje_error(self, mensaje):
        messagebox.showerror("Error de Validación", mensaje)

    def registrar(self):
        """
            Registra un nuevo usuario utilizando los datos ingresados en los campos de entrada.

            Valida los campos, muestra mensajes de error si hay problemas y guarda los datos del usuario si el registro es exitoso.
            """
        datos_usuario = self.obtener_datos_usuario()
        errores = Validador.validar_campos(datos_usuario)
        if errores:
            # Si hay errores, incluyendo campos vacíos, muestra el mensaje de error
            for campo, mensaje_error in errores.items():
                self.mostrar_mensaje_error(mensaje_error)
                return

        # Verificar si ya existe un archivo de usuario antes de permitir el registro
        if os.path.exists(self.gestor.archivo_usuario):
            messagebox.showwarning("Registro Fallido", "Ya existe un usuario registrado. Por favor inicie sesión.")
            return

        resultado_registro = self.gestor.registrar_usuario(**datos_usuario)
        if resultado_registro['exito']:
            messagebox.showinfo("Registro Exitoso", resultado_registro['mensaje'])
        else:
            messagebox.showwarning("Registro Fallido", resultado_registro['mensaje'])

    def proceso_iniciar_sesion(self):
        datos_usuario = self.obtener_datos_usuario()
        errores = Validador.validar_campos(datos_usuario)
        if errores:
            for campo, mensaje_error in errores.items():
                self.mostrar_mensaje_error(mensaje_error)
                return

        existe_archivo = os.path.exists(self.gestor.archivo_usuario)
        if existe_archivo:
            self.abrir_ventana_activacion()
            self.master.withdraw()
        else:
            self._mostrar_mensaje_archivo_usuario(existe_archivo=False)
    def obtener_datos_usuario(self):
        return {
            "nombre": self.entrada_nombre.get(),
            "apellido": self.entrada_apellido.get(),
            "telefono": self.entrada_telefono.get(),
            "centro_trabajo": self.entrada_centro_trabajo.get(),
            "cargo": self.entrada_cargo.get(),
            "usuario": self.entrada_usuario.get(),
            "email": self.entrada_email.get(),
            "contrasenia": self.entrada_contrasenia.get()
        }

    def validar_campos_requeridos(self):
        campos = [self.entrada_nombre.get(), self.entrada_apellido.get(), self.entrada_telefono.get(),
              self.entrada_centro_trabajo.get(), self.entrada_cargo.get(), self.entrada_usuario.get(),
              self.entrada_email.get(), self.entrada_contrasenia.get()]
        return all(campos)

    def on_enter(self, e):
        e.widget.config(style="Hover.TButton")

    def on_leave(self, e):
        e.widget.config(style="TButton")

    def abrir_ventana_activacion(self):
        # Crear una nueva ventana de nivel superior
        self.ventana_activacion = tk.Toplevel(self.master)
        self.ventana_activacion.configure(background="white")
        self.ventana_activacion.minsize(width=650, height=540)
        self.ventana_activacion.title("Activacion de Licencia")

        self.crear_imagen(self.ventana_activacion)
        self.llave_almacenada = self.gestor.cargar_llave_almacenada()

        # Configurar el estilo de fuente
        fuente_grande_negrita = ('Helvetica', 18, "bold")

        # Agregar una etiqueta  con el texto "Active su licencia"
        label_activacion = tk.Label(self.ventana_activacion, text="Active su licencia", background="white",
                                    font=fuente_grande_negrita)
        label_activacion.grid(row=1, column=0, padx=10, pady=10)

        # Agrege una etiqueta para el campo de la clave de licencia
        label_clave = tk.Label(self.ventana_activacion, text="Clave de licencia", background="white", font=14)
        label_clave.grid(row=2, column=0, padx=10, pady=10)

        # Agregar un campo de entrada para que el usuario ingrese la llave
        self.entrada_llave = tk.Entry(self.ventana_activacion)
        self.entrada_llave.grid(row=3, column=0, padx=10, pady=10)
        self.entrada_llave.bind("<KeyRelease>", self.habilitar_boton_siguiente)

        # Agregar una nota sobre cómo obtener la clave de licencia
        nota_clave = tk.Label(self.ventana_activacion,
                              text="Si ha adquirido la clave de licencia en línea, puede copiarla y pegarla desde el "
                                   "correo de confirmación de la compra.", background="white")
        nota_clave.grid(row=4, column=0, padx=10, pady=10)

        # Agregar un botón para enviar la llave generada
        self.boton_activar = tk.Button(self.ventana_activacion, text="Siguiente", state=tk.DISABLED,
                                       command=self.comparar_y_activar)
        self.boton_activar.grid(row=5, column=1, padx=10, pady=10)

        # Asociar evento para habilitar el botón cuando se ingrese una llave
        self.entrada_llave.bind("<KeyRelease>", self.habilitar_boton_siguiente)

        # Agregar un botón para regresar a la ventana principal
        boton_anterior = tk.Button(self.ventana_activacion, text="Anterior",
                                   command=self.volver_a_ventana_principal)
        boton_anterior.grid(row=5, column=0, padx=10, pady=10)

        # Agregar un botón para cerrar la ventana
        boton_cerrar = tk.Button(self.ventana_activacion, text="Cerrar", command=self.cerrar_ventana)
        boton_cerrar.grid(row=5, column=2, columnspan=2, padx=10, pady=10)

    def comparar_y_activar(self):
        llave_generada_ingresada = self.entrada_llave.get()
        if self.gestor.comparar_llave(llave_generada_ingresada):
            self.activar_licencia()
        else:
            messagebox.showerror("Error", "Las llaves no coinciden")

    def habilitar_boton_siguiente(self, evento=None):
        # Obtener los datos ingresados por el usuario
        nombre = self.entrada_nombre.get()
        apellido = self.entrada_apellido.get()
        telefono = self.entrada_telefono.get()
        usuario = self.entrada_usuario.get()
        email = self.entrada_email.get()
        contrasenia = self.entrada_contrasenia.get()

        # Llama al método de Gestor_Usuario para validar la llave
        if self.gestor.validar_llave(nombre, apellido, telefono, usuario, email, contrasenia):
            self.boton_activar.config(state=tk.NORMAL)
        else:
            self.boton_activar.config(state=tk.DISABLED)

    def volver_a_ventana_principal(self):
        if self.ventana_activacion:
            # Ocultar la ventana de activación
            self.ventana_activacion.withdraw()
            # Mostrar la ventana principal
            self.master.deiconify()

    def activar_licencia(self):
        # Ocultar la segunda ventana
        self.ventana_activacion.withdraw()

        # Crear una instancia de Gestor_Licencia y mostrar el EULA
        gestor_licencia = Gestor_Licencia(self.ventana_activacion)
        gestor_licencia.mostrar_eula(self.master)
