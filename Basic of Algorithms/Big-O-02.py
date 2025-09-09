lista = [ 1 , 2 , 3 , 4 , 5 ]

def l():
    print("==" * 10)

def constant(n): # O(1)
    print(n[0])


def linear(n): # O(n)
    for i in n:
        print(i)


def quadratic(n): # O(n²)
    for i in n:
        for j in n:
            print(i  , j)


def combination(n):
    # O(1) + O(n) + O(n) + O(1) = O(9) + O(n) --> O(n)

    print(n[0]) #O(1)

    for i in range(n): #O(5)
        print("test: " , i)

    for i in n: #O(n)
        print(i)

    for i in n: #O(n)
        print(i)

    print("Finishhh") #O(1)



constant(lista)
l()
linear(lista)
l()
quadratic(lista)
l()


