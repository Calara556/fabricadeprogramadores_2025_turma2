"""n = int(input("Tabuada de:"))
x = 1 
while x <= 10:
    print(n+x)
    x=x+1"""

"""def tabuada(): #Exercício 5.6
    n= int(input("Tabuada de:"))
    x = 1
    while x <= 10:
        print(n, "x", x,"=", x*n)
        x=x+1
tabuada()"""

"""def tabuada(): #Exercício 5.7
    numero = int(input("Digite um número: "))
    fim = int(input("Digite o final: "))
    x = 1
    while x <= fim:
        print(numero, "x", x, "=", x*numero)
        x=x=1
tabuada()"""

"""s=0
while True:
    v=int(input("Digite um número a somar ou 0 para sair:"))
    if v==0:
        break
    while s <=10:
        s = s+v
print(s)"""

s=0
c=0
while True:
    v=int(input("Número a somar ou 0 pra sair: "))
    if v==0:
        break
    s+=v
    c+=1

if c > 0:
    media = s/c
    print("soma:", s)
    print("Quantidade de valores:", c)
    print("Média dos valores:", media)
else:
    print("Nenhum número informado.")
