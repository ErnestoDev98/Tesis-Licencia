import tkinter as tk
from SourcePackage.Gestor_Datos.Gestor_Usuario import Gestor_Usuario
from SourcePackage.Intefaz_Grafica.Interfaz_Grafica import Interfaz_Grafica
from SourcePackage.Gestor_Licencia.Gestor_Licencia import Gestor_Licencia

class Aplicacion:
    """
       Clase principal de la aplicación que inicializa la interfaz gráfica y los gestores de usuario y licencia.

       Métodos:
       - __init__: Constructor que crea la ventana principal y las instancias de los gestores.
       - run: Inicia el bucle principal de eventos de la aplicación.
       """
    def __init__(self):
        self.root = tk.Tk()
        self.gestor = Gestor_Usuario()
        self.gestor_licencia = Gestor_Licencia()
        self.interfaz_grafica = Interfaz_Grafica(self.root, self.gestor)


    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Aplicacion()
    app.run()