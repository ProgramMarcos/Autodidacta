# pylint: disable=E0611
import sys
from PyQt6.QtCore import Qt,QDate
from PyQt6.QtWidgets import (QApplication, QWidget,QPushButton,QTextEdit,QGridLayout,QMessageBox,
                             QLabel,QDateEdit,QLineEdit,QComboBox,QFormLayout,QHBoxLayout)
from PyQt6.QtGui import QFont

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializarUI()
    
    def inicializarUI(self):
        self.setGeometry(100,100,200,600)
        self.setWindowTitle("Formulario Ingreso")
        self.crear_formulario()
        self.show()

    def crear_formulario(self):
        titulo = QLabel("Solicitud de ingreso")
        titulo.setFont(QFont("Arial",18))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.nombre_edit = QLineEdit()
        self.nombre_edit.setPlaceholderText("Nombre")
        
        self.apellido_edit = QLineEdit()
        self.apellido_edit.setPlaceholderText("Apellido")

        self.genero_selecction = QComboBox()
        self.genero_selecction.addItems(["Masculino","Femenino","Otro"])
        
        self.fecha_nacimiento_edit = QDateEdit()
        self.fecha_nacimiento_edit.setDisplayFormat("yyyy-MM-dd")
        self.fecha_nacimiento_edit.setMaximumDate(QDate.currentDate())
        self.fecha_nacimiento_edit.setCalendarPopup(True)
        self.fecha_nacimiento_edit.setDate(QDate.currentDate())

        self.telefono = QLineEdit()
        self.telefono.setPlaceholderText("+34-612345678")

        submit_button = QPushButton("Registrar")
        submit_button.clicked.connect(self.mostrar_info)

        primer_h_box = QHBoxLayout()
        primer_h_box.addWidget(self.nombre_edit)
        primer_h_box.addWidget(self.apellido_edit)

        main_form = QFormLayout()
        main_form.addRow(titulo)
        main_form.addRow("Nombre: ",primer_h_box)
        main_form.addRow("Genero: ",self.genero_selecction)
        main_form.addRow("Fecha Nacimiento: ",self.fecha_nacimiento_edit)
        main_form.addRow("Telefono: ",self.telefono)
        main_form.addRow(submit_button)

        self.setLayout(main_form)

    def mostrar_info(self):
        QMessageBox.information(self,"Informacion",
                                f"Nombre: {self.nombre_edit.text()} {self.apellido_edit.text()}\n \
                                    Genero: {self.genero_selecction.currentText()}\n \
                                        fecha: {self.fecha_nacimiento_edit.text()}\n \
                                            telefono: {self.telefono.text()}",
                                            QMessageBox.StandardButton.Ok,
                                            QMessageBox.StandardButton.Ok
                                            )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())