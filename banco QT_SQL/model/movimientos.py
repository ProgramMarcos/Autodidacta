class Transferencia():
    def __init__(self,tipo:str,documento:str,motivo:float,cantidad:int,dolares:bool,internacional:bool) :
        self.__tipo = tipo
        self.__documento = documento
        self.__motivo = motivo
        self.__cantidad = cantidad
        self.dolares = dolares
        self.internacional = internacional

    def get_tipo(self):
        return self.__tipo

    def get_documento(self):
        return self.__documento
    
    def get_motivo(self):
        return self.__motivo

    def get_cantidad(self):
        return self.__cantidad
    
class DepositoInternacional():
    def __init__(self,tipo:str,documento:str,motivo:float,cantidad:int,dolares:bool,internacional:bool,nombre1:str,nombre2:str,
                apellido1:str,apellido2:str,sexo:str,fechaNacimiento:str,lugarNacimiento:str,terminos:bool) :
        self.__tipo = tipo
        self.__documento = documento
        self.__motivo = motivo
        self.__cantidad = cantidad
        self.__dolares = dolares
        self.__internacional = internacional
        self.__nombre1 = nombre1
        self.__nombre2 = nombre2
        self.__apellido1 = apellido1
        self.__apellido2 = apellido2
        self.__sexo = sexo
        self.__fechaNacimiento = fechaNacimiento 
        self.__lugarNacimiento = lugarNacimiento
        self.__terminos = terminos



    #getters
    def get_tipo(self):
        return self.__tipo

    def get_documento(self):
        return self.__documento
    
    def get_motivo(self):
        return self.__motivo

    def get_cantidad(self):
        return self.__cantidad
    
    def get_internacional(self):
        return self.__internacional
    
    def get_dolares(self):
        return self.__dolares
    
    def get_nombre1(self):
        return self.__nombre1

    def get_nombre2(self):
        return self.__nombre2

    def get_apellido1(self):
        return self.__apellido1

    def get_apellido2(self):
        return self.__apellido2
    
    def get_sexo(self):
        return self.__sexo

    def get_fecha_nacimiento(self):
        return self.__fechaNacimiento

    def get_lugar_nacimiento(self):
        return self.__lugarNacimiento

    def get_terminos(self):
        return self.__terminos
    
    # setters
    def set_dolares(self, dolares: bool):
        self.dolares = dolares

    def set_internacional(self, internacional: bool):
        self.internacional = internacional