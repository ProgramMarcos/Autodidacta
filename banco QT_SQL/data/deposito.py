import conexion as con
from model.movimientos import DepositoInternacional
from datetime import datetime






class DepositoData():
    def __init__(self) :
        try:
            self.db = con.Conexion().conectar()
            self.cursor = self.db.cursor()
            sql_create_deposito = """CREATE TABLE IF NOT EXISTS depositos
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            cantidad NUMERIC,
                            tipo TEXT,
                            documento TEXT,
                            internacional BOOLEAN,
                            dolares BOOLEAN,
                            fecha_registro DATETIME,
                            fecha_nacimiento DATETIME,
                            motivo TEXT, 
                            pNombre TEXT,
                            sNombre TEXT,
                            pApellido TEXT,
                            sApellido TEXT,
                            sexo TEXT,
                            ciudad_nacimiento TEXT,
                            terminos BOOLEAN)"""
            self.cursor.execute(sql_create_deposito)
            self.db.commit()
            #cerrar conexión y cursor 
            self.cursor.close()
            #cerrar base de datos
            self.db.close()
            print("tabla de deposito creada")
        except Exception as ex:
            print("tabla de deposito OK", ex)

    def registrar(self,info:DepositoInternacional):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()
        self.cursor.execute("""
                                INSERT INTO depositos (
                                    cantidad, tipo, documento, dolares, internacional, fecha_registro, 
                                    fecha_nacimiento, motivo, pNombre, sNombre, pApellido, sApellido, 
                                    sexo, ciudad_nacimiento, terminos) 
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                                """, (info.get_cantidad(), info.get_tipo(), info.get_documento(),
                                    info.get_dolares(), info.get_internacional(), fecha, info.get_fecha_nacimiento().strftime('%d/%m/%Y'), 
                                    info.get_motivo(), info.get_nombre1(), info.get_nombre2(), 
                                    info.get_apellido1(), info.get_apellido2(), info.get_sexo(), 
                                    info.get_lugar_nacimiento(), info.get_terminos()))

        self.db.commit()
        if self.cursor.rowcount==1:  #elementos afectados
            return True
        else:
            return False
