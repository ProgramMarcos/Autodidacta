# pylint: disable=E0611
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow,QStatusBar,QFileDialog, QVBoxLayout, QTextEdit, 
                        QWidget, QFontDialog, QColorDialog)
from PyQt6.QtGui import QAction,QKeySequence, QTextCharFormat
from PyQt6.QtCore import QStandardPaths

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.inicializarUI()
        self.status_bar.setStyleSheet("background-color: cyan;")

    def inicializarUI(self):
        self.setGeometry(100,100,500,500)
        self.setWindowTitle("QMainWindow")
        self.generate_window()
        self.show()

    def generate_window(self):
        self.create_action()
        self.create_menu()
        self.create_content()

    def create_content(self):
        layout = QVBoxLayout()
        #widget que se guarda en el layout
        self.editor_text = QTextEdit() #self para poder acceder desde open()
        layout.addWidget(self.editor_text)
        layout.setContentsMargins(30,30,30,30) #establezco margenes
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container) #la clase padre es QMainWindow y no QWidget, 
            	                            #por lo que debemos establecer lo que se debe mostrar

                        




    def create_action(self):
        self.open_action = QAction("Abrir",self) #self para que esté anclada a la ventana que hemos creado
        self.open_action.setShortcut(QKeySequence("Ctrl+O"))
        self.open_action.setStatusTip("Abrir archivos")
        self.open_action.triggered.connect(self.open) #triggered funciona con click y con combinación de teclas (shortcut)

        self.save_action = QAction("Guardar",self) #self para que esté anclada a la ventana que hemos creado
        self.save_action.setShortcut(QKeySequence("Ctrl+S"))
        self.save_action.setStatusTip("Guardar archivos")
        self.save_action.triggered.connect(self.save)

        self.export_action = QAction("Exportar",self) #self para que esté anclada a la ventana que hemos creado
        self.export_action.setShortcut(QKeySequence("Ctrl+E"))
        self.export_action.setStatusTip("Exportar archivos")
        self.export_action.triggered.connect(self.export)

        self.font_action = QAction("Fuente",self) #self para que esté anclada a la ventana que hemos creado
        self.font_action.setShortcut(QKeySequence("Ctrl+F"))
        self.font_action.setStatusTip("Cambiar Fuente")
        self.font_action.triggered.connect(self.set_font)

        self.color_action = QAction("Color",self) #self para que esté anclada a la ventana que hemos creado
        self.color_action.setShortcut(QKeySequence("Ctrl+K"))
        self.color_action.setStatusTip("Cambiar Color")
        self.color_action.triggered.connect(self.set_color)

        self.undo_action = QAction("Deshacer", self)  # self para que esté anclada a la ventana que hemos creado
        self.undo_action.setShortcut(QKeySequence("Ctrl+Z"))
        self.undo_action.setStatusTip("Deshacer la última acción")
        self.undo_action.triggered.connect(self.undo)  # conectar con la función undo que implementes

        self.redo_action = QAction("Rehacer", self)  # self para que esté anclada a la ventana que hemos creado
        self.redo_action.setShortcut(QKeySequence("Ctrl+Y"))
        self.redo_action.setStatusTip("Rehacer la última acción deshecha")
        self.redo_action.triggered.connect(self.redo)  # conectar con la función redo que implementes


    def create_menu(self):
        menu_archivo = self.menuBar().addMenu("Archivo")
        # Añadir acciones al menú Archivo
        menu_archivo.addAction(self.open_action)   # Acción de Abrir
        menu_archivo.addAction(self.save_action)   # Acción de Guardar
        menu_archivo.addAction(self.export_action) # Acción de Exportar

        menu_editar = self.menuBar().addMenu("Editar")
        menu_editar.addAction(self.undo_action)   # Acción de Deshacer
        menu_editar.addAction(self.redo_action)   # Acción de Rehacer
        menu_editar.addAction(self.font_action)   #cambio fuente
        menu_editar.addAction(self.color_action)  #cambio de color

    def open(self):
        options = (QFileDialog.Option.DontUseNativeDialog)  #obliga a mostrar el cuadro de diálogo de PyWQt6
        initial_dir = QStandardPaths.writableLocation(
            QStandardPaths.StandardLocation.DocumentsLocation
        )
        file_type = "Text Files (*.txt);;Imagenes (*.png);;All files (*)"
        #self.file , _ = QFileDialog.getOpenFileName(self,"Open File",initial_dir,file_type,options=options)

        #si no ponemos el campo options la ventana se muestra como el explorador por defecto del sistema
        self.file , _ = QFileDialog.getOpenFileName(self,"Open File",initial_dir,file_type)
        #file guarda el contenido
        # _ guarda el tipo de archivo, como no me interesa pongo _


        with open(self.file, 'r') as file:
            self.setWindowTitle(f"QMainWindow - {self.file}") #se visualiza la ruta del archivo
            self.editor_text.setText(file.read())

    def set_color(self):
        selected_text_cursor = self.editor_text.textCursor()
        color = QColorDialog().getColor(self.editor_text.textColor(),self) #coge por color predeterminado el de la fuente seleccionada
                                                                            #self para ligarlo al mainWindow
        if color.isValid:
            if selected_text_cursor.hasSelection():
                format = QTextCharFormat()
                format.setForeground(color)
                selected_text_cursor.mergeCharFormat(format)
            else:
                self.editor_text.setTextColor(color)


    def set_font(self):
        # necesito saber el texto que se ha seleccionado con el cursor
        selected_text_cursor = self.editor_text.textCursor()
        font, ok = QFontDialog.getFont(
            self.editor_text.currentFont(),self
        ) #font es la fuente especificada por el user. OK es para saber si se presiona ok o cancelar
        if ok:
            if selected_text_cursor.hasSelection():
                format = self.editor_text.currentCharFormat() #devuelve tamaño, tipo de fuente...
                format.setFont(font) #aplico la fuente al texto seleccionado
                selected_text_cursor.mergeCharFormat(format) #aplico los cambios
            else:
                self.editor_text.setCurrentFont(font) #si no hay texto seleccionado a partir de este punto cambio la fuente

    def save(self):
        print("Guardando Cambios")
    def export(self):
        print("Exportando Archivo")
    def undo(self):
        print("Deshaciendo Cambios")
    def redo(self):
        print("Rehaciendo Cambios")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainWindow()
    sys.exit(app.exec())
