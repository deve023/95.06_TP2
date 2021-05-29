from jugador import *

def parse(path):
    cards = []

    with open(path) as File:
        cardsString = File.readline().split(',')
        
        for c in cardsString:
            cards.append(int(c))
    
    return cards

# Testeos

#print(parse('ej.txt'))

#player1 = Jugador("Jugador 1")
#player2 = Jugador("Jugador 2")

#player1.addCard(1)
#player1.addCard(3)
#player1.addCard(5)
#player2.addCard(1)
#player2.addCard(2)

#player1.scoreAdd(50)
#player2.scoreAdd(25)

#player1.info()
#player2.info()
