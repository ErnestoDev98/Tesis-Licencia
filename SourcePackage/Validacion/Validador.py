import re

# Clase Validador para validar diferentes tipos de campos de entrada
class Validador:
    @staticmethod
    def validar_nombre(nombre):
        if not re.match(r'^[a-zA-Z ]+$', nombre):
            return "El nombre debe contener solo letras y espacios."
        return None  # Si la validación es exitosa, no hay mensaje de error.

    @staticmethod
    def validar_apellido(apellido):
        if not re.match(r'^[a-zA-Z ]+$', apellido):
            return "El apellido debe contener solo letras y espacios."
        return None  # Si la validación es exitosa, no hay mensaje de error.

    @staticmethod
    def validar_correo(correo):
        patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron_correo, correo):
            return "El correo electrónico no es válido."
        return None

    @staticmethod
    def validar_contrasenia(contrasenia):
        patron_contrasenia = r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=*]).{8,}$'
        if not re.match(patron_contrasenia, contrasenia):
            return "La contraseña no cumple con los requisitos mínimos."
        return None

    @staticmethod
    def validar_telefono(telefono):
        # Valida que el teléfono tenga exactamente 8 dígitos.
        patron_telefono = r'^\d{8}$'
        if not re.match(patron_telefono, telefono):
            return "El teléfono debe contener exactamente 8 dígitos."
        return None

    @staticmethod
    def validar_campos_vacios(datos_usuario):
        # Verifica si alguno de los campos está vacío
        for campo, valor in datos_usuario.items():
            if not valor.strip():  # strip() elimina espacios en blanco al principio y al final
                return f"El campo '{campo}' no puede estar vacío."
        return None  # Si todos los campos están llenos, retorna None

    @staticmethod
    def validar_campos(datos_usuario):
        # Primero verifica si hay campos vacíos
        mensaje_vacios = Validador.validar_campos_vacios(datos_usuario)
        if mensaje_vacios:
            return {'error': mensaje_vacios}
        # Valida todos los campos del usuario utilizando los métodos definidos anteriormente.
        validaciones = {
            "nombre": Validador.validar_nombre,
            "apellido": Validador.validar_apellido,
            "email": Validador.validar_correo,
            "contrasenia": Validador.validar_contrasenia,
            "telefono": Validador.validar_telefono
        }
        errores = {}
        for campo, funcion_validacion in validaciones.items():
            mensaje_error = funcion_validacion(datos_usuario.get(campo, ''))
            if mensaje_error:
                errores[campo] = mensaje_error
        return errores if errores else None
