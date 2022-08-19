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