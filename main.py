class Jugador():
    
    def __init__(self, name):
        self.__name = name
        self.__cards = []
        self.__score = 0
    
    def scoreAdd(self, n):
        self.__score += n
    
    def score(self):
        return self.__score
    
    def name(self):
        return self.__name
    
    def cards(self):
        return self.__cards
    
    def addCard(self, c):
        self.__cards.append(c)
    
    def info(self):
        print(self.__name + ':')
        print("Cartas elegidas: ")
        print(self.__cards) # Deberia ir en junto con la linea anterior
        print("Puntos sumados: " + str(self.__score))

def parse(path):
    cards = []

    with open(path) as File:
        cardsString = File.readline().split(',')
        
        for c in cardsString:
            cards.append(int(c))
    
    return cards

print(parse('ej.txt'))

player1 = Jugador("Jugador 1")
player2 = Jugador("Jugador 2")

player1.addCard(1)
player1.addCard(3)
player1.addCard(5)
player2.addCard(1)
player2.addCard(2)

player1.scoreAdd(50)
player2.scoreAdd(25)

player1.info()
player2.info()