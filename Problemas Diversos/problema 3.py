from cgitb import text
import os
n = int(input("Ingrese un numero del 1 al 10 : "))
m = int(input("Ingrese un numero del 1 al 10 : "))
if os.path.exists(f'tabla-{n}.txt'):
    with open(f'./tabla-{n}.txt','r') as f:
        texto=f.readlines()
        for i in range(len(texto)+1):
            if(i==m):
                print(texto[i-1])
else:
    print("No existe dicha tabla")