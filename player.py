class Player():
    
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
        self.scoreAdd(c)
        self.__cards.append(c)
    
    def info(self):
        # Imprime por pantalla la data del jugador

        print( str(self.__name) + ':')

        outCards = "Cartas elegidas: "
        for i in range(0, len(self.__cards)-1):
            outCards += str(self.__cards[i]) + ", "
        outCards += str(self.__cards[-1])
        print(outCards)
        
        print("Puntos sumados: " + str(self.__score) + '\n')

