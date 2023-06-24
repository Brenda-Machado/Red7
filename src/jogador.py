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

    def initialize(self, id):
        self.id = id
    
    def atualizaVez(self):
        self.turno = not self.turno
    
    def atualizaVencedor(self):
        self.vencedor = not self.vencedor
    
    def inicioPartida(self):
        self.partida_iniciou = True
    
    def criaMao(self, baralho: dict):
        for i in range(7):
            carta = Carta(baralho[i]["cor"], baralho[i]["numero"])
            self.mao.append(carta)
