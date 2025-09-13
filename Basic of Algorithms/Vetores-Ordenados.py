# Pior caso O(n)

import numpy as np

class VetorOrdenado():
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaposicao = -1
        self.valores = np.empty(self.capacidade , dtype=int)

        #O(n)
    def imprime(self):
        if self.ultimaposicao == -1:
            print("O vetor esta vazio")
        else:
            for i in range(self.ultimaposicao + 1):
                print(f"{i}° - {self.valores[i]}")

    def insere(self, valor):
        if self.ultimaposicao == self.capacidade - 1:
            print("Capacidade maxima atingida")
            return
        
        posicao = 0
        while posicao <= self.ultimaposicao and self.valores    [posicao] < valor:
            posicao += 1

        x = self.ultimaposicao
        while x >= posicao:
            self.valores[x + 1] = self.valores [x]
            x -= 1

        self.valores[posicao] = valor
        self.ultimaposicao += 1
        



vetor = VetorOrdenado(10)
vetor.insere(1)
vetor.insere(10)
vetor.insere(8)
vetor.insere(4)
vetor.insere(2)
vetor.insere(9)
vetor.insere(12)
vetor.insere(7)
vetor.insere(5)

vetor.imprime()