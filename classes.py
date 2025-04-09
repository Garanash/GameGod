from random import shuffle

class Player:
    def __init__(self, name):
        self.name = name
        self.isAlive = True
        self.prorok = False

    def iAmProrok(self):
        self.prorok = True
        self.count = 0


class Card:
    def __init__(self, mast, number):
        self.number = number
        self.mast = mast


class God:
    def __init__(self, name, pravilo="if Card...."):
        self.name = name
        self.pravilo = pravilo

    def сourt_judge(self, obj: Card):
        return 'Правильно' if eval(self.pravilo, obj) else "Не правильно"


class GameTable:
    def __init__(self):
        self.deck_of_cards = []
        for mast in ['heart','romb','krest','tref']:
            for i in range(2,11):
                self.deck_of_cards.append(Card(mast, i))
        shuffle(self.deck_of_cards)
