import os
def tabla(numero):
    for i in range(10):
        multiplicacion=(i+1)*numero
        tabla1.append(f'{numero} x {i+1} = {multiplicacion}\n')
tabla1=[]
numero = int(input("Ingrese un numero : "))
tabla(numero)
print(tabla1)
with open(f'./tabla-{numero}.txt', 'w') as f:
    f.writelines(tabla1)