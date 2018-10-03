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
   -Oui la fonction __str__ est bien faite je l'avoue :P;
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
    
    def get_suit(self): 
        return 'T'

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
    
    def get_suit(self):
        return 'T'


    def winner(trick):
    """Allows to define the winner (1, 2, 3 or 4) of the trick"""
    #pli=[(deck[45],1),(deck[43],2),(deck[42],3),(deck[2],4)]
      Cardw=trick[0][0]
      w=trick[0][1]
      for i in range(1,4):
         if trick[i][0].color()==Cardw.color() and trick[i][0].get_value()>Cardw.get_value():
               Cardw=trick[i][0];w=trick[i][1]
         elif trick[i][0].color()!=Cardw.color() and (trick[i][0].color()== 'T'and trick[i][0].get_value()!=0):
               Cardw=trick[i][0];w=trick[i][1]
      return w
