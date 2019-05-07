#xi+1 = (a*xi+c)%m

print("Semilla:")
semilla = int(input())

print("Constante Multiplicativa:")
a = int(input())

print("Modulo:")
m = int(input())

print("Incremento:")
c = int(input())

print("Numeros requeridos:")
iteraciones = int(input())

n = 0
tabla=[]

while n < iteraciones:
    numero = (a*semilla+c) % m 
    numeroRandom = semilla/(m-1)
    tabla.append(numeroRandom)
    semilla = numero
    n = n+1

print(tabla)