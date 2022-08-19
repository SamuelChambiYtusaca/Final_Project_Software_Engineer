# Implementacion de estilos de Programacion
## Code-Golf
Constraints:

- As few lines of code as possible

```
    def get_event(self, id):
        params = {'id': id}
        rv = self.mysql_pool.execute("SELECT * from evento INNER JOIN asistente ON where asistente.id%(id)s=usuario.id%(id)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'nombre': result[1], 'link': result[2], 'detalles': result[3]}
            data.append(content)
            content.clear()
        return data
```

## Things
Constraints:

- The larger problem is decomposed into 'things' that make sense for the problem domain
- Each 'thing' is a capsule of data that exposes procedures to the rest of the world
- Data is never accessed directly, only through these procedures
- Capsules can reappropriate procedures defined in other capsules

Implementacion de la clase.


```
class PonenteModel:
    def __init__(_id, _nombre, _apellidos, _correo):
        ponente.id          = _id
        ponente.nombre      = _nombre
        ponente.apellidos   = _apellidos
        ponente.correo      = _correo
    def get_nombre(self):
        return self.nombre
    def get_apellidos(self):
        return self.apellidos
    def get_correo(self):
        return self.correo
    def set_nombre(self, _nombre):
        self.nombre = _nombre
    def set_apellidos(self, _apellidos):
        self.apellidos = _apellidos
    def set_correo(self, _correo):
        self.correo = _correo
```

## Declared Intentions

Constraints:
- Existence of a run-time typechecker
- Procedures and functions declare what types of arguments they expect
- If callers send arguments of types that aren't expected, the procedures/functions are not executed

Las diferentes conexiones y querys a la base de datos son gestionadas con try-catch para no ejecutar codigo en caso obtener un error.

```
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
            content = {'id': result[0], 'nombre': result[1], 'link': result[2], 'detalles': result[3]}
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
```

#Implementacion de practicas de codificacion legible

## Choose descriptive and unambiguous names.
Los nombres de las variables guardan relacion con la abstraccion de la funcion.
```
def get_asistente(self, id):
        params = {'id': id}
        rv = self.mysql_pool.execute("SELECT * from usuario INNER JOIN asistente ON where asistente.id%(id)s=usuario.id%(id)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'nombre': result[1], 'apellido': result[2], 'correo': result[3]}
            data.append(content)
            content = {}
        return data
```

## Be consistent. If you do something a certain way, do all similar things in the same way.
Las multiples querys a base de datos se realizan siguiendo un mismo patron.
```
    def get_asistente(self, id):
        params = {'id': id}
        rv = self.mysql_pool.execute("SELECT * from usuario INNER JOIN asistente ON where asistente.id%(id)s=usuario.id%(id)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'nombre': result[1], 'apellido': result[2], 'correo': result[3]}
            data.append(content)
            content = {}
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
```

## Do one thing.
Funciones especificas sin complicar su implementacion.
```
    def get_detalles(self):
        try: 
            rv = self.mysql_pool.execute("SELECT detalles FROM EVENTOS")
        except:
            print("Error en conexion a Base de Datos")
        data = []
        for result in rv:
            data.append(result)
        return data
```

## Don't break indentation.
La identacion indica el scope de las funciones y los staments de control de flujo correespondientes.
En python, es sumamente importante seguir este tipo de practica.

```
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
```   

## Similar functions should be close.
En la implementacion, las fuunciontes relativas a la obtencion de datos se encuentran ubicadas de forma cercana.
```
    class PonenteModel:
        def __init__(_id, _nombre, _apellidos, _correo):
            ponente.id          = _id
            ponente.nombre      = _nombre
            ponente.apellidos   = _apellidos
            ponente.correo      = _correo
        def get_nombre(self):
            return self.nombre
        def get_apellidos(self):
            return self.apellidos
        def get_correo(self):
            return self.correo
        def set_nombre(self, _nombre):
            self.nombre = _nombre
        def set_apellidos(self, _apellidos):
            self.apellidos = _apellidos
        def set_correo(self, _correo):
            self.correo = _correo
```