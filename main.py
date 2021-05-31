from player import *
from sys import argv

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
                #if setCartas in opt:
                    #print(setCartas, " ", opt[setCartas])                
                
        size += 1

    return eleccion, opt 

def eleccion_optima(setCartas, eleccion, opt):
    # devuelve el indice de setCartas de la carta a elegir

    if len(setCartas) <= 2:
        eleccion[setCartas] = setCartas.index(max(setCartas))

    else:
        #print(opt[setCartas[1:]])
        #print(opt[setCartas[:-1]])
        #print(setCartas)
        if opt[setCartas[1:]] == opt[setCartas[:-1]]:
            eleccion[setCartas] = setCartas.index(max(setCartas[0], setCartas[-1]))
        elif opt[setCartas[1:]] > opt[setCartas[:-1]]:
            eleccion[setCartas] = -1
        else:
            eleccion[setCartas] = 0

def solucion_optima(setCartas, eleccion, opt):

    if len(setCartas) <= 2:
        opt[setCartas] = max(setCartas)

    else:
        #print(setCartas)
        e1 = eleccion[setCartas]
        if e1 == 0:
            #print("e1 = 0")
            e2 = eleccion[setCartas[1:]]
            if e2 == 0:
                #print("e2 = 0")
                opt[setCartas] = setCartas[e1] + opt[setCartas[2:]]
            elif e2 == -1 or e2 == len(setCartas[1:]) - 1:
                #print("e2 = -1")
                opt[setCartas] = setCartas[e1] + opt[setCartas[1:-1]]

        elif e1 == -1 or e1 == len(setCartas) - 1:
            #print("e1 = -1")
            e2 = eleccion[setCartas[:-1]]
            #print(setCartas[:-1], e2)
            if e2 == 0:
                #print("e2 = 0")
                opt[setCartas] = setCartas[e1] + opt[setCartas[1:-1]]
            elif e2 == -1 or e2 == len(setCartas[1:]) - 1:
                #print("e2 = -1")
                opt[setCartas] = setCartas[e1] + opt[setCartas[:-2]]


def imprimirDiccionario(dic):
    for clave in dic:
        print(clave, ":", dic[clave])

def main(argv):
    assert len(argv) == 2

    cards = parse(argv[1])
    print(cards)

    eleccion, opt = armarDiccionarios(cards)

    imprimirDiccionario(eleccion)
    print("--------------")
    imprimirDiccionario(opt)

    # iterar los diccionarios y hacer  player.addCard() y player.addScore() con cada carta
    # finalmente player.info()



# Testeos

main(argv)

#player1 = Player("Jugador 1")
#player2 = Player("Jugador 2")

#player1.addCard(1)
#player1.addCard(3)
#player1.addCard(5)
#player2.addCard(1)
#player2.addCard(2)

#player1.scoreAdd(50)
#player2.scoreAdd(25)

#player1.info()
#player2.info()
