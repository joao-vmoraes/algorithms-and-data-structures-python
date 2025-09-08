class Aluno:
    def __init__(self, nota1 , nota2):
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return print(f"A media do aluno foi : {( self.nota1 + self.nota2 ) / 2}")
    
    def dados(self):
        print(f"A primeira nota foi {self.nota1}")
        print(f"A segunda nota foi {self.nota2}")

    def resultado(self):
        media = ( self.nota1 + self.nota2 ) / 2
        if media >= 7:
            return print("Aprovado")
        
        else:
            return print("Reprovado")
        
    

aluno1 = Aluno(7,8)
aluno2 = Aluno(7,6)

aluno1.media()
aluno2.media()
print("=-")
aluno1.dados()
aluno2.dados()
print("=-")
aluno1.resultado()
aluno2.resultado()
print("=-")