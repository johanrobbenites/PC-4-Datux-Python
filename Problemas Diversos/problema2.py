from cgitb import text
import os
n = int(input("Ingrese un numero del 1 al 10 : "))
if os.path.exists(f'tabla-{n}.txt'):
    with open(f'./tabla-{n}.txt','r') as f:
        texto=f.read()
        print(texto)
else:
    print("No existe dicha tabla")