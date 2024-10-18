# pylint: disable=E0611
import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton,QDockWidget,
                QStatusBar,QTabWidget,QWidget,QHBoxLayout,QVBoxLayout,QListWidget, QFileDialog,
                QListWidgetItem
                )

from PyQt6.QtMultimedia import QMediaPlayer,QAudioOutput

from PyQt6.QtGui import QAction,QKeySequence, QTextCharFormat, QGuiApplication, QPixmap, QIcon
from PyQt6.QtCore import QStandardPaths, Qt, QUrl



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.status_bar=QStatusBar()
        self.setStatusBar(self.status_bar) #añadimos status bar a mainwindow
        self.current_music_folder = ""
        #importar archivo css de estilos
        with open("ReproductorMusica/estilos.css",'r') as file:
            style = file.read()
        self.setStyleSheet(style)
        self.player = None
        self.playing_reproductor = False 


    def inicializarUI(self):
        self.setGeometry(100,100,800,500)
        self.setWindowTitle("Reproductor de música")
        self.generate_main_window()
        self.create_dock()
        self.create_action()
        self.create_menu()
        self.show()

    def generate_main_window(self):
        tab_bar = QTabWidget(self) #al poner self se asocia a mainWindow (padre)
        #qtabwidget implementa la funcionalidad de cambiar entre widgets 
        #sin hacer un stacked layout
        self.reproductor_container = QWidget()
        self.settings_container = QWidget()
        tab_bar.addTab(self.reproductor_container,
                    "Reproductor")
        tab_bar.addTab(self.settings_container,
                    "Settings")
        
        #una vez creado el tabulador debemos crear un método que genere el conmtenido
        self.generate_reproductor_tab()
        self.generate_settings_tab()

        #añadimos el contenido a un layout
        tab_h_box = QHBoxLayout()
        tab_h_box.addWidget(tab_bar)

        #añadimos layout a la página principal (solop acepta widgets)
        main_container = QWidget()
        main_container.setLayout(tab_h_box)
        self.setCentralWidget(main_container)



    def generate_reproductor_tab(self):
        main_v_box = QVBoxLayout()
        buttons_h_box = QHBoxLayout()

        song_image = QLabel()
        pixmap = QPixmap("ReproductorMusica/images/imagen.jpeg").scaled(500,500)
        song_image.setPixmap(pixmap)
        song_image.setScaledContents(True)

        button_repeat = QPushButton()
        button_repeat.setObjectName("button_repeat")
        button_before = QPushButton()
        button_before.setObjectName("button_before")
        self.button_play = QPushButton()
        self.button_play.setObjectName("button_play")
        self.button_play.clicked.connect(self.play_pause_song)
        button_next = QPushButton()
        button_next.setObjectName("button_next")
        button_random = QPushButton() 
        button_random.setObjectName("button_random")

        button_repeat.setFixedSize(40,40)
        button_before.setFixedSize(40,40)
        self.button_play.setFixedSize(50,50)
        button_next.setFixedSize(40,40)
        button_random.setFixedSize(40,40)


        buttons_h_box.addWidget(button_repeat)
        buttons_h_box.addWidget(button_before)
        buttons_h_box.addWidget(self.button_play)
        buttons_h_box.addWidget(button_next)
        buttons_h_box.addWidget(button_random)

        #hay que agregar el layout de botones al layout vertical (solo acepta widgets)
        buttons_container = QWidget()
        buttons_container.setLayout(buttons_h_box)

        main_v_box.addWidget(song_image)
        main_v_box.addWidget(buttons_container)

        #hay que unir los widgets
        self.reproductor_container.setLayout(main_v_box)

    def create_action(self):
        self.listar_musica_action = QAction('Listar Música',self , checkable=True)
        self.listar_musica_action.setShortcut(QKeySequence("Ctrl+L"))
        self.listar_musica_action.setStatusTip("Aquí puedes listar o no la música a reproducir")
        self.listar_musica_action.triggered.connect(self.list_music)
        self.listar_musica_action.setChecked(True)

        
        self.open_folder_music_action = QAction('Abrir Carpeta',self )
        self.open_folder_music_action.setShortcut(QKeySequence("Ctrl+O"))
        self.open_folder_music_action.setStatusTip("Abre tu carpeta de música")
        self.open_folder_music_action.triggered.connect(self.open_folder_music)
        


    def create_menu(self):
        self.menuBar()
        menu_file = self.menuBar().addMenu("File")
        menu_file.addAction(self.open_folder_music_action)

        menu_view = self.menuBar().addMenu("View")
        menu_view.addAction(self.listar_musica_action)

    def create_dock(self):
        self.song_list = QListWidget()
        self.dock = QDockWidget()
        self.dock.setWindowTitle("Lista de canciones")

        #establecer a donde se puede mover:
        self.dock.setAllowedAreas(
            Qt.DockWidgetArea.LeftDockWidgetArea |
            Qt.DockWidgetArea.RightDockWidgetArea
        )
        self.song_list.itemSelectionChanged.connect(self.handle_song_selection)
        self.dock.setWidget(self.song_list) #contenido del dock
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock)

    


    def list_music(self):
        if self.listar_musica_action.isChecked():
            #muestra
            self.dock.show()
        else:
            #oculta
            self.dock.hide()
    
    def open_folder_music(self):
        initial_dir = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.MusicLocation)
        self.current_music_folder = QFileDialog.getExistingDirectory(None, "Seleccione una carpeta",initial_dir)

        icon = QIcon("ReproductorMusica/images/mp3_icon.ico")

        for archivo in os.listdir(self.current_music_folder): #listar los archivos que se encuentren en la carpeta
            ruta_archivo = os.path.join(self.current_music_folder, archivo)
            if ruta_archivo.endswith(".mp3"):
                item = QListWidgetItem(archivo)
                item.setIcon(icon)
                self.song_list.addItem(item)


    def generate_settings_tab(self):
        pass

    def create_player(self):
        if self.player:  #si contiene algo (!= de None) lo borro 
            self.player.deleteLater()
        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)
        self.player.mediaStatusChanged.connect(self.media_status_changed)  #mide si hay cambios durante la reproducción
        self.audioOutput.setVolume(1.0)

    def media_status_changed(self,status):
        print('status: ',status)
        if status == QMediaPlayer.MediaStatus.LoadedMedia:  #si se carga una canción
            self.player.play()


    #slots handling
    def play_pause_song(self):
        #si se está reproduciendo el icono debe cambiar a pausa
        if self.playing_reproductor:
            self.button_play.setStyleSheet("image: url(ReproductorMusica/images/pause.png);")
            self.player.pause()
            self.playing_reproductor = False

        #si se está pausado el icono debe cambiar a play
        else:
            self.button_play.setStyleSheet("image: url(ReproductorMusica/images/play.png);")
            self.player.play()
            self.playing_reproductor = True

    def handle_song_selection(self):
        selected_item = self.song_list.currentItem()
        if selected_item:
            song_name = selected_item.data(0) #saco el nombre del archivo
            song_folder_path = os.path.join(self.current_music_folder,song_name) #uno la carpeta con el nombre del archivo para generar la ruta del archivo
            #reproducir archivo
            self.create_player()
            source = QUrl.fromLocalFile(song_folder_path)
            self.player.setSource(source)
            self.playing_reproductor = True



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())