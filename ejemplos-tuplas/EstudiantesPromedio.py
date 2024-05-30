class Promedio:
    def establecerPromedio(self,tupla):
        suma = 0
        for i in tupla:
           suma = suma + i
        suma = suma/len(tupla)
        return suma
ejTupla = (10,9,8,7,0,6,8,8,5,3)
promedio = Promedio()
print(f"El promedio General es de: {promedio.establecerPromedio(ejTupla)}")