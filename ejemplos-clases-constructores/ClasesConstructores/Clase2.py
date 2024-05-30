class Animal:
    def __init__(self, nombre,raza,habitat):
        self.nombre = nombre
        self.raza = raza
        self.habitat = habitat
    def establecerNombre(self,nombre):
        self.nombre = nombre
    def establecerRaza(self,raza):
        self.raza = raza
    def establecerHabitat(self,habitat):
        self.habitat = habitat
    def obtenerNombre(self):
        return self.nombre
    def obtenerRaza(self):
        return self.raza
    def obtenerHabitat(self):
        return self.habitat

