import conexion as con


class HistorialData:
    
    def __init__(self):
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor() 

    def buscarPorFecha(self, fechaDesde, fechaHasta, tipo, documento):
        query = """
            SELECT T.id as transaccion, D.*, T.verificado 
            FROM transferencias T
            INNER JOIN depositos D 
                ON D.tipo = T.tipo 
                AND D.documento = T.documento
                AND D.dolares = T.dolares 
                AND D.internacional = T.internacional
            WHERE T.fecha_registro >= ? 
                AND T.fecha_registro <= ? 
                AND D.documento = ? 
                AND D.tipo = ?"""
        
        # Ejecutar la consulta pasando las variables como parámetros
        self.cursor.execute(query, (fechaDesde, fechaHasta, documento, tipo))
        data = self.cursor.fetchall()
        return data
