class NumMayor:
    def encontrarMayor(self, tupla):
        mayor = tupla[0]
        for num in tupla:
            if num > mayor:
                mayor = num
        return mayor

mayor = NumMayor()

numeros = (10, 42, 78, 32, 56, 23, 85, 45, 54, 12)
print(f"El número mayor es: {mayor.encontrarMayor(numeros)}")