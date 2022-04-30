import random
import numpy as np
m = []
for x in range (1, 11):
    lista_auxiliar = []
    for y in range(1, 11):
        lista_auxiliar.append(random.randint(1, 100))
    m.append(lista_auxiliar)
    print(lista_auxiliar)
print ("Matriz 10x10")

for linha_matriz in m:
 print(linha_matriz)

soma = []
soma.append(m)
print(np.sum(soma))

print("#"*100)
matrizb = np.array(m)
soma = matrizb* 3
print("A multiplicação dos números de A")
print("Resulta na matriz b")
print("#"*100)
print(soma)