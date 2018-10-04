# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 15:23:49 2018

@author: axel
"""

"""
Remarques:
   -value correspond au numéro des cartes, point à leurs valeurs en points
   -Excuse a pour value (numéro) 0
   -Il est inutile de préciser la valeur en point des cartes lors de l'instanciation,
    la fonction init le fait tout seul.
"""

class PlayingCard:
    """Abstract parent class"""
    def __init__(self, n, p=0.5):
        assert self.__class__ is not PlayingCard
        self.__value=n
        self.__point=p
    
    def get_value(self):
        return self.__value
    def get_point(self):
        return self.__point
    def set_point(self, p):
        self.__point=p
        
    def __add__(self,other):
        return self.__point + self.__point
    
    
class Trump(PlayingCard):
    """Trump Cards"""
    def __init__(self, n):
        PlayingCard.__init__(self, n)
        if n==1 or n==21:
            self.set_point(4.5)
    
    def __str__(self):
        return "{} d'Atout".format(self.get_value())
    
    def __repr__(self):
        return "Trump({})".format(self.get_value())

    def __eq__(self, other):
        if isinstance(other,Trump):
            return self.get_value() == other.get_value()
        else:
            return False
        
    def __ne__(self, other):
        if isinstance(other,Trump):
            return self.get_value() != other.get_value()
        else:
            return True
        
    def __lt__(self, other):#Most useful (used in sorted())
        if isinstance(other,Trump):
            return self.get_value() < other.get_value()
        else:
            return False
    def __le__(self, other):
        if isinstance(other,Trump):
            return self.get_value() <= other.get_value()
        else:
            return False
    def __gt__(self, other):
        if isinstance(other,Trump):
            return self.get_value() > other.get_value()
        else:
            return True
        
    def __ge__(self, other):
        if isinstance(other,Trump):
            return self.get_value() >= other.get_value()
        else:
            return True

    
class Card(PlayingCard):
    """Spades, Hearts, Diamonds and Clovers"""
    def __init__(self, n, s):
        PlayingCard.__init__(self, n)
        self.__suit=s
        if n>10:
            self.set_point(n-9.5)
    
    def get_suit(self):
        return self.__suit
    
    def __str__(self):#Les dictionnaires à leur plein potentiel
        return "{} de {}".format({11:'Valet',12:'Cavalier',13:'Reine',14:'Roi'}
                                 .get(self.get_value(),self.get_value()),
                                 {'S':"Pique",'H':"Coeur",'D':"Carreau",'C':"Trèfle"}[self.__suit])
    
    def __repr__(self):
        return "Card({},{})".format(self.get_value(), self.__suit)


class Excuse(PlayingCard):
    """The Fool or Excuse"""    
    def __init__(self,n=0,p=4.5):
        PlayingCard.__init__(self, n, p)
    
    def __str__(self):
        return "Excuse"
    
    def __repr__(self):
        return "Excuse()"
      
      
class Player():
    """Abstract parent class for both IA and Human"""
    def __init__(self, hand, score):
        assert self.__class__ is not Player
        self.__hand= hand
        self.__score= score
    
    def get_hand(self):
        return self.__hand
    def get_score(self):
        return self.__score
    def set_hand(self, hand):
        self.__hand=hand
    def set_score(self, score):
        self.__score=score

    def playing_trump(self, trick):
        hand=self.get_hand()[:]
        L=[el for el in hand if not isinstance(el,Card)]
        if L==[]:
            return hand
        else:
            best_trump=trick[winner(trick)].get_value()
            K=[el for el in L if el.get_value()>best_trump]
            """
                if K==[]:
                    return L
                else:
                    return K
            """
            return K or L

    def playable_cards(self, trick):
        hand=self.get_hand()[:]
        if trick==[]:
            return hand
        elif isinstance(trick[0], Trump):
            return self.playing_trump(trick)
        elif isinstance(trick[0], Card):
            suit=trick[0].get_suit()
            L=[el for el in hand if (isinstance(el,Card) and el.get_suit()==suit)]
            """
            if L!=[]:
                return L
            else:
                return self.playing_trump(T)
            """
            return L or self.playing_trump(trick)
        elif isinstance(trick[0], Excuse):
            return self.playable_cards(trick[1:])


class IA(Player):
    def __init__(self, hand, score):
        Player.__init__(self, hand, score)
    def play(self,trick):
        playable_cards=Player.playable_cards(self, trick)
        self.get_hand().remove(playable_cards[0])
        return (playable_cards[0])

                
class Human(Player):
    def __init__(self, hand, score):
        Player.__init__(self, hand, score)
    
    def play(self, trick):
        if trick==[]:
            print("C'est à vous de commencer le pli. Voici votre main:\n")
        #else:
          #  print("Rappel:les cartes jouées sont:")
           # for el in trick:
            #    print(el)
        print("\nVous pouvez jouer les cartes suivantes:")
        playable_cards=Player.playable_cards(self, trick)
        for i, el in enumerate(playable_cards):
            print(str(i)+"-->"+str(el))
        while True:
            try:
                card=int(input("Votre choix? (Indice Python)"))
            except ValueError:
                print("Entrez un numéro de la liste.")
                continue
            if card>=len(playable_cards) or card<0:
                    print("Entrez un numéro de la liste.")
            else:
                break
        self.get_hand().remove(playable_cards[card])
        return (playable_cards[card])
 

"""Fonctions"""

def bidding():
    return random.randint(0,3), ['Petite','Prise','Garde','Garde sans','Garde contre'][random.randint(0,4)]

   
def score():
    pass

   
def create_deck():
    """Creates a tarot deck of 78 cards"""
    L=[]
    for i in range(1, 22):
        L.append(Trump(i))
    for s in ('S', 'H', 'D', 'C'):
        for i in range(1, 15):
            L.append(Card(i, s))
    L.append(Excuse())
    return L

   
def deal(players):
    deck=create_deck()
    random.shuffle(deck)
    dog=deck[-6:]
    for i in range(4):
        (players[i]).set_hand(deck[(i*18):((i+1)*18)])
    return dog


def create_players(n):
    players=[]
    for i in range(n):
        players.append(IA([],0))
    for i in range(4-n):
        players.append(Human([],0))
    return players


def winner(trick):
    """Allows to define the winner (0, 1, 2, or 3) of the trick"""
    w_card=trick[0]
    w=0
    for i in range(1,len(trick)):
        if isinstance(w_card, Trump):
            if isinstance(trick[i], Trump) and trick[i]>w_card:
                w_card, w=trick[i], i
        if isinstance(w_card, Card):
            if isinstance(trick[i], Trump):
                w_card, w=trick[i], i
            elif isinstance(trick[i], Card) and trick[i].get_suit()==w_card.get_suit() and trick[i].get_value()>w_card.get_value():
               w_card, w=trick[i], i
        if isinstance(w_card, Excuse):
                w_card, w=trick[i], i
    return w


def game(players,dealer):
    dog=deal(players)
    bidder, bid= bidding()#Identifier bidder & defender 
    print("Le joueur "+str(bidder)+" a pris un contrat: "+bid)
    first_player=(dealer+1)%4
    points_bidder, points_defenders= 0,0
    for i in range(18):
        trick=[]
        for i in range(4):
            index=(first_player+i)%4
            card=players[index].play(trick)
            print("Joueur "+str(index)+" a joué "+str(card))
            trick.append(card)
        first_player=(first_player+winner(trick))%4
        print ("Le joueur "+str(first_player)+" a remporté ce pli\n")
        if first_player==bidder:
            points_bidder+=sum(card.get_point() for card in trick)
        else:
            points_defenders+=sum(card.get_point() for card in trick)
    print("Points bidder: "+str(points_bidder))
    print("Points defenders: "+str(points_defenders))
    print("Points chien: "+str(sum(card.get_point() for card in dog)))
    score()
    

def begin_game(n):
    game_on=True
    dealer=random.randint(0,3)
    players=create_players(n)
    while game_on:
        game(players,dealer)
        game_on=bool('True'==input("Pour continuer, écrire True"))
        dealer+=1


if __name__ == '__main__':
    begin_game(3)#L'humain sera le joueur 3
