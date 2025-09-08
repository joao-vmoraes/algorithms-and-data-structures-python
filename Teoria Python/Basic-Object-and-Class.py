###
# Agrupamente de objetos similares que apresentam os mesmos atributos e métodos
# 
# como se fosse um molde de boneco de gesso, ou forma de bolo, etc.
# 
# Exemplo:
#   Classe: Cachorro
#   objeto: Puggy
#   objeto: Pastor Alemão###


class triangulo:
    def __init__(self , lado1, lado2 , lado3, base, altura):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura
    
t1 = triangulo(2, 1 ,3, 4 , 3)

print(t1.lado1)
print(t1.lado2)
print(t1.lado3)
print(t1.base)
print(t1.altura)

print("-=-=-=-=-")

t2 = triangulo(4 ,5 ,6 ,3 ,6)
print(t2.lado1)
print(t2.lado2)
print(t2.lado3)