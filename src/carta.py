"""
Brenda Silva Machado
Descrição: Classe que define cada carta do jogo
"""

class Carta():
    def __init__(self, cor : int, numero : int):
        self.cor = cor
        self.numero = numero

    def getCor(self):
        return self.cor
    
    def getNumero(self):
        return self.numero