class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return f"Usuario(nombre='{self.nombre}')"