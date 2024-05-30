class ClaseEstudiantes:
    def __init__(self):
        self.estudiantes = []

    def agregarEstudiante(self, nombre, calificacion):
        self.estudiantes.append((nombre, calificacion))

    def calificacionPromedio(self):
        suma = 0
        for estudiante in self.estudiantes:
            suma += estudiante[1]
        return suma / len(self.estudiantes)


estudiantes = ClaseEstudiantes()


estudiantes.agregarEstudiante("Lady", 10)
estudiantes.agregarEstudiante("Aldrin", 5)
estudiantes.agregarEstudiante("Manuel", 6)

promedio = estudiantes.calificacionPromedio()
print(f"Calificación promedio de la clase: {promedio:.2f}")
