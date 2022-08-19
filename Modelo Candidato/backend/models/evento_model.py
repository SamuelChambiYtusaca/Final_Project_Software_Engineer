from backend.models.connection_pool import MySQLPool

class EventoModel:
    def __init__(self):
        try:
            self.mysql_pool = MySQLPool()
        except:
            print("Error en conexion a Base de Datos")
    def get_event(self, id):
        params = {'id': id}
        try:
            rv = self.mysql_pool.execute("SELECT * from evento INNER JOIN asistente ON where asistente.id%(id)s=usuario.id%(id)s", params)                
        except:
            print("Error en conexion a Base de Datos")
        data = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'nombre': result[1], 'apellido': result[2], 'correo': result[3]}
            data.append(content)
            content.clear()
        return data
    
    def get_all_events(self):
        try:
            rv = self.mysql_pool.execute("SELECT * FROM EVENTOS")
        except:
            print("Error en conexion a Base de Datos")
        data = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'nombre': result[1], 'link': result[2], 'detalles': result[3]}
            data.append(content)
            content.clear()
        return data

    def get_link(self):
        try:
            rv = self.mysql_pool.execute("SELECT link FROM EVENTOS")
        except:
            print("Error en conexion a Base de Datos")
        data = []
        for result in rv:
            data.append(result)
        return data

    def get_detalles(self):
        try: 
            rv = self.mysql_pool.execute("SELECT detalles FROM EVENTOS")
        except:
            print("Error en conexion a Base de Datos")
        data = []
        for result in rv:
            data.append(result)
        return data

