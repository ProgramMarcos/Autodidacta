# pylint: disable=E0611


import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication,
                                QLabel, QWidget,QLineEdit,
                                QPushButton, QMessageBox,
                                QCheckBox, QDialog)
from PyQt6.QtGui import QFont, QPixmap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100,100,500,500)
        self.setWindowTitle("Ventana Principal")
        self.generar_contenido()

    def generar_contenido(self):
        image_path = 'mapacho.png'

        try:
            with open(image_path):
                image_label = QLabel(self)
            
                # Cargar la imagen
                pixmap = QPixmap(image_path)
                
                # Ajustar el tamaño de la imagen a la ventana
                scaled_pixmap = pixmap.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatio, 
                                              Qt.TransformationMode.SmoothTransformation)
                
                # Asignar la imagen escalada al QLabel
                image_label.setPixmap(scaled_pixmap)
                
                # Ajustar el QLabel para que ocupe todo el espacio disponible
                image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                image_label.resize(self.size())  # Opcional: asegura que el QLabel ocupe todo el espacio
        except FileNotFoundError as e:
            QMessageBox.warning(self,"Error",f"Imagen no encontrada: {e}",
                                        QMessageBox.StandardButton.Close,
                                        QMessageBox.StandardButton.Close)
        except Exception as e:
            QMessageBox.warning(self,"Error",f'Error en el mainview: {e}',
                                        QMessageBox.StandardButton.Close,
                                        QMessageBox.StandardButton.Close)

