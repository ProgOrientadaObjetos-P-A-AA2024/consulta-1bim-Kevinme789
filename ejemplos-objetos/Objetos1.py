class Motos:
    def __init__(self,matricula,color,modelo):
        self.matricula=matricula
        self.color=color
        self.modelo=modelo
    def obtener_matricula(self):
        return self.matricula
    def obtener_modelo(self):
        return self.modelo
    def obtener_color(self):
        return self.color
moto1 = Motos("MB12EC","rojo","Suzuki")
moto2  = Motos("17HFPS","azul","Nissan")
print(f"Matricula de la Primera Moto:{moto1.obtener_matricula()}\nModelo:{moto1.obtener_modelo()}\n"
      f"Color:{moto1.obtener_color()}")
print(f"Matricula de la Segunda Moto:{moto2.obtener_matricula()}\nModelo:{moto2.obtener_modelo()}\n"
      f"Color:{moto2.obtener_color()}")
