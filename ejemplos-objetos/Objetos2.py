class Persona:
    def __init__(self, nombre, apellido, edad,estatura):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.estatura = estatura
    def obtener_nombre(self):
        return self.nombre
    def obtener_apellido(self):
        return self.apellido
    def obtener_edad(self):
        return self.edad
    def obtener_estatura(self):
        return self.estatura
persona1 = Persona("Kevin", "Robles", "18", "169")
persona2= Persona("Marcelo", "Espinoza", "25", "175")
print(f"Nombre:{persona1.obtener_nombre()}\nApellido:{persona1.obtener_apellido()}\nEdad:{persona1.obtener_edad()}\n"
      f"Estatura:{persona1.obtener_estatura()}cm")
print(f"Nombre:{persona2.obtener_nombre()}\nApellido:{persona2.obtener_apellido()}\nEdad:{persona2.obtener_edad()}\n"
      f"Estatura:{persona2.obtener_estatura()}cm")