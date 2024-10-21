import conexion as con
from model.movimientos import Transferencia
from datetime import datetime


class TransferenciaData():
    def __init__(self) :
        try:
            self.db = con.Conexion().conectar()
            self.cursor = self.db.cursor()
            sql_create_transferencias = """CREATE TABLE IF NOT EXISTS transferencias
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            cantidad NUMERIC,
                            tipo TEXT,
                            documento TEXT,
                            internacional BOOLEAN,
                            dolares BOOLEAN,
                            fecha_registro DATETIME,
                            verificado BOOLEAN ,
                            motivo TEXT)"""
            self.cursor.execute(sql_create_transferencias)
            self.db.commit()
            #cerrar conexión y cursor
            self.cursor.close()
            #cerrar base de datos
            self.db.close()
            print("tabla transferencias creada")
        except Exception as ex:
            print("tabla transferencias OK", ex)

    def registrar(self,info:Transferencia):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()
        self.cursor.execute("""
                    INSERT INTO transferencias values(null,'{}','{}','{}','{}','{}','{}','{}','{}')
                    """.format(info.get_cantidad(),info.get_tipo(),info.get_documento(),
                            info.internacional,info.dolares, fecha, False, info.get_motivo()))
        self.db.commit()
        if self.cursor.rowcount==1:  #elementos afectados
            return True
        else:
            return False
