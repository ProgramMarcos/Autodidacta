# pylint: disable=E0611
from PyQt6 import uic #convierte el diseño en un archivo python
from PyQt6.QtWidgets import QMessageBox,QLabel,QPushButton,QTableWidgetItem
from datetime import datetime, date, timedelta

from data.usuario import UsuarioData
from model.usuario import Usuario
from gui.registro import RegistroWindow

from model.movimientos import Transferencia
from data.Transferencia import TransferenciaData

from data.ciudad import CiudadData

from model.movimientos import DepositoInternacional
from data.deposito import DepositoData

from data.historial import HistorialData

class MainWindow():
    def __init__(self) :
        self.main = uic.loadUi("gui/main.ui")
        self.initGUI()
        self.main.showMaximized()

    def initGUI(self):
        self.main.btnRegistrar_Transferencias.triggered.connect(self.abrirRegistro)
        self.main.btnReportar_Transferencias.triggered.connect(self.abrirDeposito)
        self.main.btnHistorial_de_Transferencias.triggered.connect(self.abrirHistorial)
        self.registro = uic.loadUi("gui/registro.ui")
        self.deposito = uic.loadUi("gui/deposito.ui")
        self.historial = uic.loadUi("gui/historial.ui")
        


        
##########   Transferencias
    def abrirRegistro(self):
        self.registro.btnRegistrar.clicked.connect(self.registrarTransferencia)
        self.registro.show()


    def registrarTransferencia(self):
        if self.registro.cbTipo.currentText() == "--- Seleccione una opción":
            mBox =QMessageBox()
            mBox.setText("Debe seleccionar el tipo de documento")
            mBox.exec()
            self.registro.cbTipo.setFocus()
        elif len(self.registro.txtDocumento.text()) < 4:
            mBox =QMessageBox()
            mBox.setText("Debe debe ingresar una identificación válida")
            mBox.exec()
            self.registro.txtDocumento.setFocus()
        elif self.registro.cbMotivo.currentText() == "--- Seleccione una opción":
            mBox =QMessageBox()
            mBox.setText("Debe seleccionar el motivo")
            mBox.exec()
            self.registro.cbMotivo.setFocus()
        elif not self.registro.txtCantidad.text().isnumeric() :
            mBox =QMessageBox()
            mBox.setText("La cantidad debe ser indicada en Números")
            mBox.exec() 
            self.registro.txtCantidad.setText("0")
            self.registro.txtCantidad.setFocus()
        else:
            transferencia = Transferencia(
                tipo=self.registro.cbTipo.currentText(),
                documento=self.registro.txtDocumento.text(),
                motivo=self.registro.cbMotivo.currentText(),
                cantidad=float(self.registro.txtCantidad.text()),
                dolares=self.registro.checkDolares.isChecked(),
                internacional=self.registro.checkInternacional.isChecked()
            )
            mBox = QMessageBox()
            objData = TransferenciaData()
            if objData.registrar(info=transferencia):
                mBox.setText("Transferencia Registrada")
                self.limpiarCamposTransferencias()

            else:
                mBox.setText("Transferencia No Registrada")
            mBox.exec() 

    def limpiarCamposTransferencias(self):
        self.registro.cbTipo.setCurrentIndex(0) #borrar combo box (en realidad se pone en 0: --- Seleccionar Tipo)
        self.registro.cbMotivo.setCurrentIndex(0)
        self.registro.txtDocumento.setText("")
        self.registro.txtCantidad.setText("")
        self.registro.checkDolares.setChecked(False)
        self.registro.checkInternacional.setChecked(False)
        self.registro.txtDocumento.setFocus()

##########   Deposito
    
    def abrirDeposito(self):
        self.deposito.btnRegistrar.clicked.connect(self.registrarDeposito)
        self.deposito.show()
        self.deposito.txtFecha.setDate(date.today())  #<--- el combo siempre muestra inicialmente el día actual
        self.llenarComboComunidades()


    def llenarComboComunidades(self):
        objData = CiudadData()
        datos = objData.listaCiudades()
        for item in datos:
            self.deposito.cbLugar.addItem(item[1]) #agrego el nombre de la ciudad al cb



    def registrarDeposito(self):
        #self.deposito.txtFecha.setDate(date.today())
        mBox = QMessageBox()
        fecha_actual = date.today()
        fecha_mayoria_edad = date(fecha_actual.year - 18,fecha_actual.month,fecha_actual.day)
        if (not self.deposito.txtDocumento.text() or not self.deposito.txtPrimerNombre.text()
                or not self.deposito.txtPrimerApellido.text() or not self.deposito.txtCantidad.text()
                or self.deposito.cbSexo.currentIndex() == 0 or self.deposito.cbLugar.currentIndex() == 0
                or self.deposito.cbMotivo.currentIndex() == 0 or self.deposito.cbTipo.currentIndex() == 0):
            
            mBox.setText("Debe rellenar los campos obligatorios (*)")
            mBox.exec()
            
        elif self.deposito.txtFecha.date().toPyDate() > fecha_mayoria_edad:
            mBox.setText("Debe de ser mayor de edad")
            mBox.exec()
            self.deposito.txtFecha.setFocus()
        elif not self.deposito.checkTerminos.isChecked():
            mBox.setText("Debe aceptar condiciones")
            mBox.exec()
            self.deposito.checkTerminos.setFocus()
            
        elif not self.deposito.txtCantidad.text().isnumeric():
            mBox.setText("La cantidad debe ser indicada en Números")
            mBox.exec() 
            self.deposito.txtCantidad.setText("0")
            self.deposito.txtCantidad.setFocus()
        elif  float(self.deposito.txtCantidad.text()) <= 0:
            mBox.setText("La cantidad debe ser mayor a 0 (cero) ")
            mBox.exec() 
            self.deposito.txtCantidad.setText("0")
            self.deposito.txtCantidad.setFocus()

        else:
            fechaN=self.deposito.txtFecha.date().toPyDate()

            if self.deposito.checkInternacional.isChecked() == 1:
                internacional = 'True'
            else:
                internacional = 'False'  
            if self.deposito.checkDolares.isChecked() == 1:
                dolares = 'True'
            else:
                dolares = 'False'

            deposito = DepositoInternacional(
                cantidad=float(self.deposito.txtCantidad.text()),
                tipo=self.deposito.cbTipo.currentText(),
                documento=self.deposito.txtDocumento.text(),
                motivo=self.deposito.cbMotivo.currentText(),
                dolares=dolares,
                internacional=internacional,
                nombre1=self.deposito.txtPrimerNombre.text(),
                nombre2=self.deposito.txtSegundoNombre.text(),
                apellido1=self.deposito.txtPrimerApellido.text(),
                apellido2=self.deposito.txtSegundoApellido.text(),
                sexo=self.deposito.cbSexo.currentText(),
                lugarNacimiento=self.deposito.cbLugar.currentText(), 
                terminos=self.deposito.checkTerminos.isChecked(),
                fechaNacimiento= fechaN            
            )
            objData = DepositoData()
            if objData.registrar(info=deposito):
                mBox.setText("Deposito Registrado")
                self.limpiarCamposDeposito()

            else:
                mBox.setText("Deposito No Registrado")
            mBox.exec()

    

    def limpiarCamposDeposito(self):
        self.deposito.cbTipo.setCurrentIndex(0)  # Restablecer combo box a la opción inicial
        self.deposito.cbMotivo.setCurrentIndex(0)
        self.deposito.cbSexo.setCurrentIndex(0)
        self.deposito.cbLugar.setCurrentIndex(0)
        self.deposito.txtDocumento.setText("")
        self.deposito.txtPrimerNombre.setText("")
        self.deposito.txtSegundoNombre.setText("")
        self.deposito.txtPrimerApellido.setText("")
        self.deposito.txtSegundoApellido.setText("")
        self.deposito.txtCantidad.setText("0")
        self.deposito.checkTerminos.setChecked(False)
        self.deposito.checkDolares.setChecked(False)
        self.deposito.checkInternacional.setChecked(False)
        self.deposito.txtFecha.setDate(date.today())  # Restablecer la fecha al día actual <-- self.abrirDeposito()
        self.deposito.txtDocumento.setFocus()


##########   Historial
    def abrirHistorial(self):
        self.historial.btnBuscar.clicked.connect(self.buscar)

        # Configurar el ancho de las columnas de la tabla de historial
        self.historial.tblHistorial.setColumnWidth(0, 50)   # ID de la transacción
        self.historial.tblHistorial.setColumnWidth(1, 250)  # Nombre completo
        self.historial.tblHistorial.setColumnWidth(2, 100)  # Cantidad en USD/EUR
        self.historial.tblHistorial.setColumnWidth(3, 250)  # Tipo de transferencia (Nacional/Internacional)
        self.historial.tblHistorial.setColumnWidth(4, 150)  # Fecha de la transferencia
        self.historial.tblHistorial.setColumnWidth(5, 120)  # Verificación (Verificado/No Verificado)

        # Mostrar la ventana de historial
        self.historial.show()

        # Configurar las fechas predeterminadas del rango
        self.historial.txtFechaHasta.setDate(date.today() + timedelta(days=1))  # Fecha final (mañana)
        self.historial.txtFechaDesde.setDate(date.today() - timedelta(days=365))  # Fecha inicial (hace un año)

        # Llamar a la función que llena la tabla de historial
        self.llenarTablaHistorial()


    def buscar(self):
        histo = HistorialData()
        
        # Obtener los datos del historial
        data = histo.buscarPorFecha(
            self.historial.txtFechaDesde.date().toPyDate(), 
            self.historial.txtFechaHasta.date().toPyDate(),
            self.historial.cbTipo.currentText(),
            self.historial.txtDocumento.text()
        )

        # Preparar la tabla con el número de filas
        fila = 0
        self.historial.tblHistorial.setRowCount(len(data))

        # Rellenar la tabla con los datos obtenidos
        for i in data:
            # ID de la transacción
            self.historial.tblHistorial.setItem(fila, 0, QTableWidgetItem(str(i[0])))

            # Nombre completo
            nombre_completo = "{} {} {} {}".format(i[10], i[11], i[12], i[13])
            self.historial.tblHistorial.setItem(fila, 1, QTableWidgetItem(nombre_completo))

            # Cantidad en dólares o euros
            if str(i[6]) == 'True':  # Si es dólares
                self.historial.tblHistorial.setItem(fila, 2, QTableWidgetItem("USD " + str(i[2])))
            else:
                self.historial.tblHistorial.setItem(fila, 2, QTableWidgetItem(str(i[2]) + "€"))

            # Tipo de transferencia (Internacional o Nacional)
            if  i[5] == 'True':  # Si es internacional
                self.historial.tblHistorial.setItem(fila, 3, QTableWidgetItem("Internacional - " + str(i[9])))
            else:
                self.historial.tblHistorial.setItem(fila, 3, QTableWidgetItem("Nacional - " + str(i[9])))

            # Fecha de la transferencia
            self.historial.tblHistorial.setItem(fila, 4, QTableWidgetItem(str(i[7])))

            # Verificación de la transferencia
            if i[17] == 'True' :  # Comprobar si está verificado
                self.historial.tblHistorial.setItem(fila, 5, QTableWidgetItem("Verificado"))
            else:
                self.historial.tblHistorial.setItem(fila, 5, QTableWidgetItem("No Verificado"))

            # Incrementar la fila para la siguiente iteración
            fila += 1


    def llenarTablaHistorial(self):
        pass
