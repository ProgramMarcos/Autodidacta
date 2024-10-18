# pylint: disable=E0611


import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QWidget,
                                QLabel, QWidget,QLineEdit,
                                QPushButton, QMessageBox,
                                QCheckBox)
from PyQt6.QtGui import QFont, QPixmap

from registro import RegistrarUsuarioView
from main import MainWindow

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()
    def inicializar_ui(self):
        self.setGeometry(100,100,350,250)
        self.setWindowTitle("MI LOGIN")
        self.generar_formulario()
        self.show()
    def generar_formulario(self):
        self.is_logged = False

        user_label = QLabel(self)
        user_label.setText("Usuario:")
        user_label.setFont(QFont('Arial',10))
        user_label.move(20,54)

        #ponemos self para que sea accesible
        self.user_input = QLineEdit(self) #donde vamos a meter la info
        self.user_input.resize(250,24)
        self.user_input.move(90,50)

        pasword_label = QLabel(self)
        pasword_label.setText("Pàsword:")
        pasword_label.setFont(QFont('Arial',10))
        pasword_label.move(20,86)

        #ponemos self para que sea accesible
        self.pasword_input = QLineEdit(self) #donde vamos a meter la info
        self.pasword_input.resize(250,24)
        self.pasword_input.move(90,82)
        self.pasword_input.setEchoMode(QLineEdit.EchoMode.Password)
        

        self.check_view_psw = QCheckBox(self)
        self.check_view_psw.setText("Ver Contraseña")
        self.check_view_psw.move(90,110)
        self.check_view_psw.toggled.connect(self.mostrar_psw)

        login_button = QPushButton(self)
        login_button.setText('Login')
        login_button.resize(320,24)
        login_button.move(20,140)
        login_button.clicked.connect(self.login)

        register_button = QPushButton(self)
        register_button.setText('Registrarse')
        register_button.resize(320,24)
        register_button.move(20,180)
        register_button.clicked.connect(self.registrar_usuario)
    def mostrar_psw(self,clicked):
        if clicked:
            self.pasword_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
             self.pasword_input.setEchoMode(QLineEdit.EchoMode.Password)

    def login(self):
        users = []
        user_path = 'usuarios.txt'

        try:
            with open(user_path, 'r') as f:
                for linea in f:
                    users.append(linea.strip("\n"))
                login_information = f"{self.user_input.text()},{self.pasword_input.text()}"

                if login_information in users:
                    QMessageBox.information(self,"Inicio sesión","Inicio sesión exitoso",
                                            QMessageBox.StandardButton.Ok,
                                            QMessageBox.StandardButton.Ok)
                    self.is_logged=True
                    self.close()
                    self.open_main_window()
                else:
                    QMessageBox.warning(self,"Error","Usuario no registrado",
                                        QMessageBox.StandardButton.Close,
                                        QMessageBox.StandardButton.Close)


        except FileNotFoundError as e:
            QMessageBox.warning(self,"Error",f"Base de datos de usuario no encontrada: {e}",
                                        QMessageBox.StandardButton.Close,
                                        QMessageBox.StandardButton.Close)
        except Exception as e:
            QMessageBox.warning(self,"Error",f"Error en el servidor: {e}",
                                        QMessageBox.StandardButton.Close,
                                        QMessageBox.StandardButton.Close)


            

    def registrar_usuario(self):
        self.new_user_form = RegistrarUsuarioView()
        self.new_user_form.show()

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec())
