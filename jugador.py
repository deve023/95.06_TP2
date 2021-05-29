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