import hashlib
import json


class Gestor_Usuario:
    def __init__(self):
        self._usuario = None
        self.archivo_usuario = "usuario.json"
        self.cargar_usuario_existente()

    def cargar_usuario_existente(self):
        try:
            with open(self.archivo_usuario, "r") as archivo:
                self._usuario = json.load(archivo)
        except FileNotFoundError:
            # No crear un archivo nuevo si no existe uno previo
            self._usuario = None

    def cargar_llave_almacenada(self):
        # Cargar la llave almacenada desde el archivo JSON
        try:
            with open('usuario.json', 'r') as archivo_json:
                datos = json.load(archivo_json)
                return datos.get('llave')  # Utiliza get para evitar KeyError si 'llave' no está en datos
        except (FileNotFoundError, json.JSONDecodeError):
            # Si el archivo no existe o hay un error al cargarlo, simplemente retorna None
            # La llave se creará y guardará durante el proceso de registro
            return None

    def generar_llave(self, nombre, apellido, telefono, usuario, email, contrasenia):
        # Crear una cadena unica con todos los datos del usuario
        datos_usuario = f"{nombre}{apellido}{telefono}{usuario}{email}{contrasenia}"
        # Generar un hash de los datos
        llave_unica = hashlib.sha256(datos_usuario.encode()).hexdigest()
        return llave_unica

    def validar_llave(self, nombre, apellido, telefono, usuario, email, contrasenia):
        llave_generada = self.generar_llave(nombre, apellido, telefono, usuario, email, contrasenia)
        llave_almacenada = self.cargar_llave_almacenada()
        return llave_generada == llave_almacenada

    def comparar_llave(self, llave_generada_ingresada):
        llave_almacenada = self.cargar_llave_almacenada()
        return llave_generada_ingresada == llave_almacenada

    def registrar_usuario(self, nombre, apellido, telefono, centro_trabajo, cargo, usuario, email, contrasenia):
        # Verificar si ya existe un usuario registrado
        if self._usuario is not None:
            return {'exito': False, 'mensaje': "Ya existe un usuario registrado."}
        # Generar la llave única basada en los datos proporcionados
        llave = self.generar_llave(nombre, apellido, telefono, usuario, email, contrasenia)
        # Crear el diccionario de datos del usuario
        self._usuario = {
            "nombre": nombre,
            "apellido": apellido,
            "telefono": telefono,
            "centro_trabajo": centro_trabajo,
            "cargo": cargo,
            "usuario": usuario,
            "email": email,
            "contraseña": contrasenia,
            "llave": llave
        }
        # Guardar los datos del usuario en un archivo JSON
        self.guardar_usuario(self._usuario)
        return {'exito': True, 'mensaje': "Usuario registrado con éxito."}

    def guardar_usuario(self, usuario):
        # Guardar los datos del usuario en un archivo JSON
        with open(self.archivo_usuario, "w") as archivo:
            json.dump(usuario, archivo, indent=4)

    def mostrar_usuario(self):
        return self._usuario

