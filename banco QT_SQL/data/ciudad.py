import conexion as con


class CiudadData():

        

    def listaCiudades(self):
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()
        res = self.cursor.execute("SELECT * FROM comunidades ORDER BY nombre")
        comunidades = res.fetchall() #[0] = id, [1]= nombre...
        return comunidades


