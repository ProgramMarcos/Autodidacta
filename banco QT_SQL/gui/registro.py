# pylint: disable=E0611
from PyQt6 import uic #convierte el diseño en un archivo python


from data.usuario import UsuarioData
from model.usuario import Usuario
#from gui.main import MainWindow

class RegistroWindow():
    def __init__(self) :
        self.v = uic.loadUi("gui/registro.ui")
        #self.initGUI()
        self.v.show()
    