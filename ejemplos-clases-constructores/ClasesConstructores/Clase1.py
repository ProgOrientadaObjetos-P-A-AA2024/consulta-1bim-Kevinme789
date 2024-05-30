# Clase
class Automovil:
    # Constructor
    def __init__(self,marca,anio,modelo):
        self.marca = marca
        self.anio = anio
        self.modelo = modelo
    def establecer_modelo(self,modelo):
        self.modelo = modelo
    def establecer_marca(self,marca):
        self.marca = marca
    def establecer_anio(self,anio):
        self.anio = anio
    def obtenerMarca(self):
        return self.marca
    def obtenerModelo(self):
        return self.modelo
    def obtenerAnio(self):
        return self.anio