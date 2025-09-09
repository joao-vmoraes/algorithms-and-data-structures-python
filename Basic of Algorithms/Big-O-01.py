import timeit as t
import math
import numpy as np
import matplotlib.pyplot as plt


def lista1(): #O(n)
    lista = []
    for i in range(1000):
        lista += [i]
    return lista



def lista2(): # O(1)
    return range(1000)

#=============================================#

n = np.linspace(1 ,10 , 100)

labels = ["Constant" , "Logarithmic" , "Linear" , "Log Linear" , "Quadratic" , "Cubic" , "Exponential"]

big_o = [np.ones(n.shape) , np.log(n) , n , n * np.log(n) , n ** 2 , n ** 3 , 2 ** n ]

plt.figure(figsize=(10,8))
plt.ylim(0, 100)

for i in range (len(big_o)):
    plt.plot(n , big_o[i] , label = labels[i])
plt.legend()
plt.ylabel("Runtime")
plt.xlabel("n")

plt.show()