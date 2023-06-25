"""
Brenda Silva Machado
Descrição: Classe que define a paleta de cores
"""

class Paleta():
    def __init__(self):
        self.corAtual = 1
    
    def getCorAtual(self):
        return self.corAtual
    
    def mudaRegra(self, cor):
        self.corAtual = cor