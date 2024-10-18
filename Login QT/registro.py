# pylint: disable=E0611


import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QWidget,
                                QLabel, QWidget,QLineEdit,
                                QPushButton, QMessageBox,
                                QCheckBox, QDialog)
from PyQt6.QtGui import QFont, QPixmap


class RegistrarUsuarioView(QDialog):
    #CONSTRUCTOR
    def __init__(self):
        super().__init__()
        self.setModal(True) #cuando ejecute y el user quioera ejecutar con otra ventana no pueda
        self.generar_formulario()
    def generar_formulario(self):
        self.setGeometry(100,100,350,250)
        self.setWindowTitle("Registration Window")

        user_label = QLabel(self)
        user_label.setText("Usuario:")
        user_label.setFont(QFont('Arial',10))
        user_label.move(20,44)

        #ponemos self para que sea accesible
        self.user_input = QLineEdit(self) #donde vamos a meter la info
        self.user_input.resize(250,24)
        self.user_input.move(90,40)

        psw1_label = QLabel(self)
        psw1_label.setText("Introduzca Contraseña:")
        psw1_label.setFont(QFont('Arial',10))
        psw1_label.move(20,74)

        self.psw1_input = QLineEdit(self) #donde vamos a meter la info
        self.psw1_input.resize(120,24)
        self.psw1_input.move(200,70)
        self.psw1_input.setEchoMode(QLineEdit.EchoMode.Password)

        
        psw2_label = QLabel(self)
        psw2_label.setText("Repita Contraseña:")
        psw2_label.setFont(QFont('Arial',10))
        psw2_label.move(20,104)

        self.psw2_input = QLineEdit(self) #donde vamos a meter la info
        self.psw2_input.resize(120,24)
        self.psw2_input.move(200,100)
        self.psw2_input.setEchoMode(QLineEdit.EchoMode.Password)

        create_button = QPushButton(self)
        create_button.setText("Crear")
        create_button.resize(150,32)
        create_button.move(20,170)
        create_button.clicked.connect(self.crear_Usuario)

        cancel_button = QPushButton(self)
        cancel_button.setText("Cancelar")
        cancel_button.resize(150,32)
        cancel_button.move(170,170)
        create_button.clicked.connect(self.cancelar_creacion)

    def cancelar_creacion(self):
        self.close()

    def crear_Usuario(self):
        user_path = 'usuarios.txt'
        usuario = self.user_input.text()
        psw1 = self.psw1_input.text()
        psw2 = self.psw2_input.text()

        if psw1 == '' or psw2 == '' or usuario == '':
            QMessageBox.warning(self,'Error','Faltan Campos',
                                QMessageBox.StandardButton.Close,  #boton que se muestra
                                QMessageBox.StandardButton.Close)  #boton por defecto
        elif psw1 != psw2:
             QMessageBox.warning(self,'Error','Las contraseñas no coinciden',
                                QMessageBox.StandardButton.Close,  #boton que se muestra
                                QMessageBox.StandardButton.Close)  #boton por defecto
        else:
            try:
                with open(user_path,'a+') as f:
                    f.write(f"{usuario},{psw1}\n")
                QMessageBox.information(self,'Creado con exito',
                                         'Usuario creado correctamente',
                                         QMessageBox.StandardButton.Ok,
                                         QMessageBox.StandardButton.Ok)
                self.close()
            except FileNotFoundError as e:
                QMessageBox.warning(self,'Error',f'La base de datos de usuario no existe:{e}',
                                QMessageBox.StandardButton.Close,  #boton que se muestra
                                QMessageBox.StandardButton.Close)  #boton por defecto

