#xi+1 = (a*xi)%m

print("Semilla:")
semilla = int(input())

print("Constante Multiplicativa:")
a = int(input())

print("Modulo:")
m = int(input())

print("Numeros requeridos:")
iteraciones = int(input())

n = 0
tabla=[]

while n < iteraciones:
    numero = (a*semilla) % m 
    tabla.append(numero)
    semilla = numero
    n = n+1

print(tabla)