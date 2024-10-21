class Usuario():
    def __init__(self,nombre='',usuario='',clave='') :
        self.__nombre = nombre
        self.__usuario = usuario
        self.__clave = clave

    def get_usuario(self):
        return self.__usuario

    def get_clave(self):
        return self.__clave

        