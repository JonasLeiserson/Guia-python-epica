#ej 1
def PARometro(lista):
    ListaPar = []
    for Numero in lista:
        if Numero % 2 == 0:
            ListaPar.append(Numero)
    print(ListaPar)
    return ListaPar

#ej 2
def NumMasGrande(lista):
    if len(lista) == 0:
        print("lista vacia 0")
        return 0

    else: 
        lista.sort(reverse=True)
        print(lista[0])
        return lista
    
#ej 3
def NumMasChico(lista):
    if len(lista) == 0:
        print("lista vacia 0")
        return 0
        
    else: 
        lista.sort()
        print(lista[0])
        return lista
#ej 4
def Promediador(lista):
    if len(lista) == 0:
        print("lista vacia 0")
        return 0

    else: 
        numerosDeElementos = len(lista)
        SumaDeNumerosLista = sum(lista)
        Promedio = SumaDeNumerosLista / numerosDeElementos
        print(Promedio)
        return Promedio
#ej 5
def NumMayorIndivisible(lista):
    if len(lista) == 0:
        print("lista vacia 0")
        return 0

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
    return mayor
#ej 6
def UnidorDeListas(lista):
    if len(lista) == 0:
        print("lista vacia ")
        return 0
    
    listaTotal = [ElementoDeListas for sublistas in lista for ElementoDeListas in sublistas]
    print(listaTotal)
    return listaTotal

#ej 7
def UnidorDeListasConMayorDeCadaUna(lista):
    listaTotal = []
    if len(lista) == 0:
        print("lista vacia ")
        return 0
    
    for sublistas in lista: 
        sublistas.sort(reverse=True)
        listaTotal.append(sublistas[0])
    print(listaTotal)
    return listaTotal
#ej 8
def es_vocal(letra):
    
    LetraEnNumero = ord(letra.lower()) 
    return LetraEnNumero in (97, 101, 105, 111, 117)

#ej9
def es_vocalString(Oracion):
    resultado = map(FiltrarConsonantes, Oracion)
    return list(filter(None, resultado))

def FiltrarConsonantes(letra):
    if not es_vocal(letra):
        return letra
    return None

#ej10

def FusionadorDeListas(listaDeListas):
    ListaTotal = [[], []]
    for sublistas in listaDeListas:
        for i in range(2):
            ListaTotal[i].insert(len(ListaTotal[i]), sublistas[i])
    return ListaTotal
