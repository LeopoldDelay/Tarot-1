# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 15:23:49 2018

@author: axel
"""

"""Version 2: Fonctions de comparaison pour Trump objet"""
"""L'excuse tjrs perdante? Non car on doit jouer l'excuse si on n'a pas d'atout?
L'atout tjrs supérieur
2 cartes de couleur non comparables?
En théorie on a seulement besoin de > et <: les cartes sont toutes différentes
"""
"""Version 3: Fonction get_suit() pour Card"""

"""
Ces 4 classes formeront la base de notre travail.
S'il y le moindre souci avec la manière dont c'est implémenté, ou même avec
le nom des variables, il faut le signaler dès que possible!
"""
"""Remarques:
    -value correspond au numéro des cartes, point à leurs valeurs en points
    -Excuse a pour value (numéro) 0
    -Il est inutile de préciser la valeur en point des cartes lors de l'instanciation,
     la fonction init le fait tout seul.
    -Oui la fonction __str__ est bien faite je l'avoue :P
"""


class PlayingCard:
    """This abstract class is not very useful yet, but will get more methods later"""
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


if __name__ == '__main__':
    """
    deck=create_deck()
    print(deck)
    print(deck[1])
    print(deck[75])
    print(deck[77],deck[77].get_value(),deck[77].get_point())
    print(deck[0],deck[0].get_value(),deck[0].get_point())
    print(deck[1],deck[1].get_value(),deck[1].get_point())
    print(deck[20],deck[20].get_value(),deck[20].get_point())
    print(deck[30],deck[30].get_value(),deck[30].get_point()) 
    print(deck[31],deck[31].get_value(),deck[31].get_point())
    print(deck[32],deck[32].get_value(),deck[32].get_point()) 
    print(deck[33],deck[33].get_value(),deck[33].get_point())
    print(deck[34],deck[34].get_value(),deck[34].get_point())
    """
    print(Trump(21)>Trump(10))
    print(Trump(21)>=Trump(10))
    print(Trump(21)!=Trump(10))
    print(Trump(21)>Card(10,'H'))
    #print(Card(11,'H')>Card(10,'H'))
    print(Trump(21)+Card(14,'H'))