"""
Brenda Silva Machado
Descrição: Classe que define o jogador
"""

from carta import Carta

class Jogador():
    def __init__(self):
        self.id = ""
        self.vencedor = False
        self.mao = []
        self.turno = False
        self.ja_baixou = False
        self.ja_mudou = False
        self.partida_iniciou = False
    
    def getId(self):
        return self.id
    
    def getVencedor(self):
        return self.vencedor
    
    def getMao(self):
        return self.mao
    
    def getTurno(self):
        return self.turno
    
    def getJaBaixou(self):
        return self.ja_baixou
    
    def getJaMudou(self):
        return self.ja_mudou
    
    def getPartidaIniciou(self):
        return self.partida_iniciou 

    def initialize(self, id):
        self.id = id
    
    def atualizaVez(self):
        self.turno = not self.turno
    
    def atualizaVencedor(self):
        self.vencedor = not self.vencedor
    
    def setjaBaixou(self, valor):
        self.ja_baixou = valor
    
    def setjaMudou(self, valor):
        self.ja_mudou = valor
    
    def inicioPartida(self):
        self.partida_iniciou = True
    
    def atualizaMao(self, carta):
        for item in self.mao:
            if item == carta:
                self.mao.remove(item)
                break
    
    def criaMao(self, baralho: dict):
        for i in range(7):
            carta = Carta(baralho[i][0], baralho[i][1])
            self.mao.append(carta)
