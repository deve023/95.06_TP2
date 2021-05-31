from player import *
from sys import argv

# Lee el archivo de entrada y devuelve un arreglo con las cartas en juego
def parse(path):
    cards = []

    with open(path) as File:
        cardsString = File.readline().split(',')
        
        for c in cardsString:
            value = 0
            try:
                value = int(c)
            except ValueError:
                continue # saltea si no es un digito
            cards.append(value)
    return cards

# Arma los diccionarios opt y eleccion
def armarDiccionarios(array):
    #clave: subarreglo    valor: ÍNDICE de carta a sacar
    opt = {}
    eleccion = {}
    size = 1

    while size <= len(array):
        for i in range(len(array)-size+1):
            subarray = []
            #setCartas = "" 

            for j in range(size):
                 subarray.append(array[i+j])

            setCartas = tuple(subarray)
            #
            #Esto agrega a los diccionarios un nuevo subarreglo con su carta óptima a sacar y su puntaje.
            #La idea es que tenga en cuenta cómo debería seguir sacando cartas hasta llegar al
            #caso base para saber cuál es la óptima a sacar en este subarreglo
            if setCartas not in opt:
                eleccion_optima(setCartas, eleccion, opt)
                solucion_optima(setCartas, eleccion, opt)                
                
        size += 1

    return eleccion, opt 

# Guarda en eleccion la eleccion optima de setCartas
# Guarda la posicion de la carta a elegir en setCartas
def eleccion_optima(setCartas, eleccion, opt):
    # devuelve el indice de setCartas de la carta a elegir

    if len(setCartas) <= 2:
        eleccion[setCartas] = setCartas.index(max(setCartas))

    else:
        if opt[setCartas[1:]] == opt[setCartas[:-1]]:
            eleccion[setCartas] = setCartas.index(max(setCartas[0], setCartas[-1]))
        elif opt[setCartas[1:]] > opt[setCartas[:-1]]:
            eleccion[setCartas] = -1
        else:
            eleccion[setCartas] = 0

# Guarda en opt el mejor puntaje que se puede obtener de setCartas
def solucion_optima(setCartas, eleccion, opt):

    if len(setCartas) <= 2:
        opt[setCartas] = max(setCartas)

    else:
        e1 = eleccion[setCartas]
        if e1 == 0:
            e2 = eleccion[setCartas[1:]]
            if e2 == 0:
                opt[setCartas] = setCartas[e1] + opt[setCartas[2:]]
            elif e2 == -1 or e2 == len(setCartas[1:]) - 1:
                opt[setCartas] = setCartas[e1] + opt[setCartas[1:-1]]

        elif e1 == -1 or e1 == len(setCartas) - 1:
            e2 = eleccion[setCartas[:-1]]
            if e2 == 0:
                opt[setCartas] = setCartas[e1] + opt[setCartas[1:-1]]
            elif e2 == -1 or e2 == len(setCartas[1:]) - 1:
                opt[setCartas] = setCartas[e1] + opt[setCartas[:-2]]

# Agrega a firstPlayer y secondPlayer las cartas optimas que van eligiendo
def cartasElegidas(X, eleccion, firstPlayer,  secondPlayer):
    X = tuple(X)

    for i in range(len(X)):
        e = eleccion[X]
        
        if i % 2 == 0:
            firstPlayer.addCard(X[e])
        else:
            secondPlayer.addCard(X[e])

        if e == 0:
            X = X[1:]
        else:
            X = X[:-1]

def main(argv):
    assert len(argv) == 2

    cards = parse(argv[1])

    eleccion, opt = armarDiccionarios(cards)

    firstPlayer = Player("Jugador 1")
    secondPlayer = Player("Jugador 2")

    cartasElegidas(cards, eleccion, firstPlayer, secondPlayer)

    firstPlayer.info()
    secondPlayer.info()


main(argv)
