#ej 1
def PARometro(lista):
    ListaPar = []
    for Numero in lista:
        if Numero % 2 == 0:
            ListaPar.append(Numero)
    print(ListaPar)

#ej 2
def NumMasGrande(lista):
    if len(lista) == 0:
        print("lista vacia 0")

    else: 
        lista.sort(reverse=True)
        print(lista[0])
#ej 3
def NumMasChico(lista):
    if len(lista) == 0:
        print("lista vacia 0")

    else: 
        lista.sort()
        print(lista[0])

#ej 4
def Promediador(lista):
    if len(lista) == 0:
        print("lista vacia 0")

    else: 
        numerosDeElementos = len(lista)
        SumaDeNumerosLista = sum(lista)
        Promedio = SumaDeNumerosLista / numerosDeElementos
        print(Promedio)

#ej 5
def NumMayorIndivisible(lista):
    if len(lista) == 0:
        print("lista vacia 0")

    else: 
        mayor = None
        for Numero in lista:
            Esdivisible = False
            for NumeroPeroAhoraBueno in lista:
                if Numero % NumeroPeroAhoraBueno == 0 and Numero != NumeroPeroAhoraBueno:
                    Esdivisible = True
                    break
                if not Esdivisible:
                    if mayor is None or Numero > mayor: 
                        mayor = Numero
                        
    print(mayor)

#ej 6
def UnidorDeListas(lista):
    if len(lista) == 0:
        print("lista vacia ")
    listaTotal = [ElementoDeListas for sublistas in lista for ElementoDeListas in sublistas]
    print(listaTotal)

#ej 7
def UnidorDeListasConMayorDeCadaUna(lista):
    listaTotal = []
    if len(lista) == 0:
        print("lista vacia ")
    
    for sublistas in lista: 
        sublistas.sort(reverse=True)
        listaTotal.append(sublistas[0])
    print(listaTotal)

#ej 8
def es_vocal(letra):
    ord(letra) 
    

es_vocal("a")