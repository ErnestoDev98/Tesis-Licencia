from tkinter import messagebox, ttk
import tkinter as tk

# Clase principal para gestionar la licencia de usuario final (EULA)
class Gestor_Licencia:
    def __init__(self, segunda_ventana=None):
        # Inicialización de variables y configuración de estilo
        self.ventana_eula = None
        self.var_acepto = tk.IntVar(value=0)  # Inicialmente no seleccionado
        self.segunda_ventana = segunda_ventana
        self.configurar_estilo()

    def configurar_estilo(self):
        # Configuración del estilo de los widgets
        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 9), background='white')

    def mostrar_eula(self, master):
        """
            Muestra el acuerdo EULA en una nueva ventana.

            Parámetros:
            - master: widget padre desde el cual se invoca la ventana del EULA.
            """
        # Mostrar el acuerdo EULA en una nueva ventana
        self.crear_ventana_eula(master)
        self.agregar_scrollbar_y_texto()
        self.agregar_check_acepto()
        self.agregar_botones()

    def crear_ventana_eula(self, master):
        # Crear la ventana para el EULA
        self.ventana_eula = tk.Toplevel(master)
        self.ventana_eula.title("Acuerdo de Licencia de Usuario Final")
        self.ventana_eula.configure(bg='white')
        self.ventana_eula.grid_rowconfigure(0, weight=1)
        self.ventana_eula.grid_columnconfigure(0, weight=1)

    def agregar_scrollbar_y_texto(self):
        # Agregar scrollbar y área de texto para el contenido del EULA
        scrollbar = tk.Scrollbar(self.ventana_eula)
        scrollbar.grid(row=0, column=1, sticky='ns')
        texto_eula = tk.Text(self.ventana_eula, wrap='word', yscrollcommand=scrollbar.set)
        scrollbar.config(command=texto_eula.yview)
        self.cargar_contenido_eula(texto_eula)
        texto_eula.grid(row=0, column=0, sticky='nsew')
        texto_eula.config(state='disabled')

    def cargar_contenido_eula(self, widget_texto):
        # Cargar el contenido del EULA desde un archivo
        try:
            with open('eula.txt', 'r', encoding='utf-8') as file:
                eula_content = file.read()
            widget_texto.insert(tk.INSERT, eula_content)
        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo EULA no se encuentra.")

    def agregar_check_acepto(self):
        # Agregar checkbox para aceptar los términos y condiciones
        check_acepto = tk.Checkbutton(self.ventana_eula, text="Acepto los términos y condiciones.",
                                      variable=self.var_acepto,
                                      command=self.actualizar_estado_boton_aceptar,
                                      fg="green", selectcolor="light grey", activeforeground="green")
        check_acepto.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def actualizar_estado_boton_aceptar(self):
        # Actualizar el estado del botón 'Aceptar' basado en el checkbox
        estado = tk.NORMAL if self.var_acepto.get() else tk.DISABLED
        self.boton_aceptar.config(state=estado)

    def agregar_botones(self):
        # Agregar botones para aceptar, cancelar o volver
        self.boton_aceptar = ttk.Button(self.ventana_eula, text="Aceptar", state=tk.DISABLED,
                                        command=self.aceptar_eula)
        self.boton_aceptar.grid(row=2, column=0, padx=10, pady=10)

        boton_cancelar = ttk.Button(self.ventana_eula, text="Cerrar", command=self.cancelar)
        boton_cancelar.grid(row=2, column=1, padx=10, pady=10)

        boton_volver = ttk.Button(self.ventana_eula, text="Volver", command=self.volver_a_segunda_ventana)
        boton_volver.grid(row=2, column=2, columnspan=2, padx=10, pady=10)

    def volver_a_segunda_ventana(self):
        # Volver a la segunda ventana y cerrar la actual
        if self.ventana_eula:
            self.ventana_eula.destroy()
            self.segunda_ventana.deiconify()

    def cancelar(self):
        # Cerrar la ventana actual
        self.ventana_eula.destroy()

    def aceptar_eula(self):
        """
            Maneja la acción de aceptar el EULA.

            Si el usuario acepta el EULA, muestra un mensaje de agradecimiento y cierra la ventana.
            Si el usuario no acepta el EULA, muestra una advertencia indicando que es necesario aceptar para continuar.
            """
        # Aceptar el EULA y cerrar la ventana
        if self.var_acepto.get() == 1:
            messagebox.showinfo("EULA", "Gracias por aceptar los términos. Puede continuar con el uso del software.")
            self.ventana_eula.destroy()
        else:
            messagebox.showwarning("EULA", "Debe aceptar los términos para usar el software.")
