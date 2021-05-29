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

def main(argv):
    assert len(argv) == 2

    cards = parse(argv[1])
    print(cards)


# Testeos

main(argv)

#player1 = Player("Jugador 1")
#player2 = Player("Jugador 2")

#player1.addCard(1)
#player1.addCard(3)
#player1.addCard(5)
#player2.addCard(1)
#player2.addCard(2)

#player1.setScore(50)
#player2.setScore(25)

#player1.info()
#player2.info()
