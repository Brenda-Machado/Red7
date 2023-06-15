"""
Brenda Silva Machado
Descrição: Classe que define a mesa do jogo
"""

from paleta import Paleta
from partida import Partida
from carta import Carta

class Mesa():
    def __init__(self):
        self.mesaJogador1 = {}
        self.mesaJogador2 = {}
        self.paleta = None
        self.regraAtual = 0
    
    def getMesaJogador1(self):
        return self.mesaJogador1
    
    def getMesaJogador2(self):
        return self.mesaJogador2
    
    def mudaRegra(self, cor):
        self.regraAtual = cor
        self.paleta.mudaRegra(cor)
    
    def inicioPartida(self):
        self.paleta = Paleta()
    
    def avaliaVitoria(self):
        pass