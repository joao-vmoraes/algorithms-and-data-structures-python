class listaLinearEsquencialCrescente:
    def __init__(self, tamanho):
        self.ultimo = 0
        self.tamanho = tamanho
        self.lista = [None] * tamanho 

    def insertionSort(self):
        for j in range(1 , self.ultimo):
            chave = self.lista[j]
            i = j - 1
            while i >= 0 and self.lista[i] > chave:
                self.lista[i + 1] = self.lista[i]
                i = i - 1
            self.lista[i + 1] = chave

    def imprimir(self):
        print("[", end="")
        for i in range(self.tamanho):
            if self.lista[i] != None:
                print(f"{self.lista[i]}, " , end="")
            else:
                print(f"NIL, ", end="")
        print("]")


    def buscar(self, numero):
        achou = None
        for i in range(self.ultimo):
            if numero == self.lista[i]:
                achou = i
                break
        return achou
    
    def inserir(self, numero):
        if self.ultimo == self.tamanho:
            listaSuporte = self.duplicarTamanhoLista()
            self.lista = listaSuporte.lista
            self.tamanho = listaSuporte.tamanho
        self.lista[self.ultimo] = numero
        self.ultimo = self.ultimo + 1
        self.insertionSort()

    def remover(self, numero):
        indice = self.buscar(numero)

        if indice is not None:
            self.lista[indice] = None
            for i in range(indice, self.ultimo):
                self.lista[i] = self.lista[i + 1]
            self.ultimo -= 1
        else:
            print("Elemento invalido ou nao encontrado.")

    def duplicarTamanhoLista(self):
        novaListaLinear = listaLinearEsquencialCrescente(self.tamanho * 2)
        novaListaLinear.ultimo = self.ultimo
        for i in range(self.ultimo):
            novaListaLinear.lista[i] = self.lista[i]
        return novaListaLinear


def linha():
    print("=" * 20)

