import re
regla1='^[456]\d{15}$'
lista_repetidos=['0000','1111','2222','3333','4444','5555','6666','7777','8888','9999']
valor=0
def validar(lista,valor):
    for i in lista:
        if re.match(regla1,i):
            for j in lista_repetidos:
                if re.search(j,i):  
                    valor=1
            if valor==1:
               print("Invalid")
               valor=0
            else:
                print("Valid")
                valor=0
        else:
            print("Invalid")

with open('./numeros.txt') as f:
    data = f.readlines()
lista=[]
valor2=0
for n in data:
    n=n.strip()
    l=n.split('-')
    for k in l:
        if not(len(k)==16 or len(k)==4):
            valor2=1
    if(valor2==1):
        l.append('999')
    valor2=0
    n=''.join(l)
    lista.append(n)

validar(lista,valor)