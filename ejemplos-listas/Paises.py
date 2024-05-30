class Paises:
    def __init__(self, paises):
        self.paises = paises

    def paisesInicialP(self):
        paises = []
        for pais in self.paises:
            if pais[0].lower() == 'p':
                paises.append(pais)
        return paises

listaPaises = ["Argentina", "Brasil", "Chile", "Perú", "Paraguay", "Bolivia", "Panamá", "Colombia", "Portugal"]


paisesP = Paises(listaPaises)

paises = paisesP.paisesInicialP()
print("Países que comienzan con 'P':")
for pais in paises:
    print(pais)