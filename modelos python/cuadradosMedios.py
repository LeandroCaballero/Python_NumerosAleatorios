print("Semilla:")
semilla = int(input())

print("Numeros requeridos:")
iteraciones = int(input())
n=0
tabla=[]

if semilla%100 ==  0:
    semilla = semilla + 13

while n < iteraciones:  
    cuadrado = semilla * semilla
    string = str(cuadrado) #se convierte el numero en cadena
    longitud = len(string)

    if longitud == 7:
        cuadradoCorregido = "0" + string        #agregar un 0 al inicio
        centro = cuadradoCorregido[2:6]         #tomo los 4 del medio
        entero = int(centro)                    #se convierte a entero
        if entero % 100 == 0:                   #if para saber si termina en doble 0
            semilla = entero + 13
        else:
            semilla = entero
        tabla.append(entero)                    #agregar el numero a la tabla
        n = n+1

    elif longitud == 6:
        cuadradoCorregido = "00" + string
        centro = cuadradoCorregido[2:6]         #tomo los 4 del medio
        entero = int(centro)
        if entero % 100 == 0:
            semilla = entero + 13
        else:
            semilla = entero
        tabla.append(entero)
        n = n+1

    elif longitud == 5:
        cuadradoCorregido = "000" + string
        centro = cuadradoCorregido[2:6]         #tomo los 4 del medio
        entero = int(centro)
        if entero % 100 == 0:
            semilla = entero + 13
        else:
            semilla = entero
        tabla.append(entero)
        n = n+1

    else:
        centro = string[2:6]                    #tomo los 4 del medio
        entero = int(centro)
        if entero % 100 == 0:
            semilla = entero + 13
        else:
            semilla = entero
        tabla.append(entero)
        n = n+1

print(tabla)

#cuando aparece un numero de 3 cifras es porque la tercer cifra de los 8 numeros es 0, ejemplo 12045877 apareceria el 458
#https://www.academia.edu/11094142/3.-Generaci%C3%B3n_de_n%C3%BAmeros_aleatorios