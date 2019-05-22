#xi+1 = (a*xi)%m

#print("Comienzo del intervalo:")
#a = int(input())
#
#print("Final del intervalo:")
#b = int(input())
#
#print("Semilla:")
#semilla = int(input())
#
#print("Constante Multiplicativa:")
#const = int(input())
#
#print("Modulo:")
#m = int(input())
#
#print("Numeros requeridos:")
#iteraciones = int(input())
#n = 0
#
#while n < iteraciones:
#    numero = (const*semilla) % m 
#    r1 = (numero*(b-a))+a
#    print(r1)
#    semilla = numero
#    n = n+1

#---------------------------------------------------------------------
print("Semilla:")
semilla = int(input())
k=int(input("Numero mayor a 2: "))
min=int(input("Ingrese valor minimo: "))
max=int(input("Ingrese valor maximo: "))
num=int(input("Ingrese cantidad de valores deseados: "))

c=10*k+1
m=max

i=0
while i<num:
    semilla=(c*semilla)%m

    if semilla>min:
        print(semilla)
        i=i+1