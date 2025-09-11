import numpy as np

class VetorNaoOrdenado:
    def __init__(self , capacidade):
        self.capacidade = capacidade
        self.ultimaposicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self): # O(n)
        if self.ultimaposicao == -1:
            print("O vetor esta vazio")
        else:
            for i in range(self.ultimaposicao + 1):
                print(i , "° - " , self.valores[i])

    def insere(self, valor): # O(1) - O(2)
        if self.ultimaposicao == self.capacidade - 1:
            print("Capacidade maxima ja foi atingida")
        else:
            self.ultimaposicao += 1
            self.valores[self.ultimaposicao] = valor


vetor = VetorNaoOrdenado(5)

vetor.imprime()

vetor.insere(3)
vetor.insere(7)
vetor.insere(1)
vetor.insere(8)
vetor.insere(6)


vetor.imprime()