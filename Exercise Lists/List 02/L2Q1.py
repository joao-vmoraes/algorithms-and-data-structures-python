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

def digiteInt(mensagem):
    while True:
        try:
            opcao = int(input(f"{mensagem}"))
            return opcao
        except:
            print("ERRO: Tipo de dado invalido")

def inicializacao():
    return digiteInt("Digite o tamanho da sua lista: ")

def menu():
    linha()
    print("[1] - Listar")
    print("[2] - Procurar")
    print("[3] - Inserir")
    print("[4] - Remover")
    print("[5] - Sair")


#MAIN
tamanho = inicializacao()
ListaLinear = listaLinearEsquencialCrescente(tamanho)

while True:
    menu()
    opcao = digiteInt("Escolha sua opcao: ")
    linha()

    if opcao == 1:
        ListaLinear.imprimir()
    elif opcao == 2:
        numero = digiteInt("Digite um numero a ser procurado na lista: ")
        print(f"O numero esta na posicao: {ListaLinear.buscar(numero)}")
    elif opcao == 3:
        numero = digiteInt("Digite um numero a ser inserido na lista: ")
        ListaLinear.inserir(numero)
    elif opcao == 4:
        numero = digiteInt("Digite um numero a ser removido na lista: ")
        ListaLinear.remover(numero)
    elif opcao == 5:
        print("Ate logo!")
        break
    else:
        continue