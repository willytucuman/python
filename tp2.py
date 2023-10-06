#1  Dada la lista listaEjemplo = [12,” María”,” fecha de hoy”,-12.3,”Tucuman”] presentarla en pantalla.
#2  Con la lista del ejercicio 1 usando índices negativos presente el elemento-12.3 y usando índices positivos presente el elemento “María”
#               -5      -4           -3   -2        -1
#               0       1       2           3       4
#listaEjemplo = [12,"Maria","Fecha de hoy",-12.3,"Tucuman"]
#print(listaEjemplo[inicio:fin:step])
#print(listaEjemplo[-3:-1])
#print(listaEjemplo[1:2])

#obtener factorial del numero
"""num = int(input("Ingrese su numero para factorerar: "))
i=1
while num > 0:
    i*=num
    num-=1
print(i)"""

#3  Usando la lista del ejercicio 1 y mediante particionado de listas presente todos los elementos entre “María” y “Tucumán” sin incluir a ninguno de estos dos elementos.
"""listaEjemplo = [12,"Maria","Fecha de hoy",-12.3,"Tucuman"]
particionado = listaEjemplo[2:4]
print(particionado)
"""
#4  Dado los siguientes números 12,23,45,21,”A”,-24 por medio de instrucciones agréguelos al final de la lista del ejercicio 1 presente ambas listas en pantalla
"""listaEjemplo = [12,"Maria","Fecha de hoy",-12.3,"Tucuman"]
lista2= [12,23,45,21,"A",-24]
print(listaEjemplo+lista2)"""

#5 Construya una lista que contenga los números del 1 al 20 usando un ciclo While
"""i = 1
lista_1_al_20 = []
while i<=20:
    lista_1_al_20.append(i)
    i+=1
print(lista_1_al_20)"""

#6 Con la lista anterior presente en pantalla el elemento que se encuentran en la cuarta posición y el índice del elemento que vale 8 usando instrucciones
"""i = 1
lista_1_al_20 = []
while i<=20:
    lista_1_al_20.append(i)
    i+=1
print(lista_1_al_20)
print(lista_1_al_20[4])
print(lista_1_al_20.index(8))
"""

#8 Genere una lista que contenga los números del 1 al 100 usando un ciclo While a continuación pida a el usuario un numero entre 1 y 100 y presente el elemento que se encuentra en esa posición y la posición del elemento que vale el valor ingresado por el usuario.
"""N = int(input("Ingrese un numero entre 1 y 100: "))
i = 1
lista_1_al_100 = []
while i<=100:
    lista_1_al_100.append(i)
    i+=1
#print(lista_1_al_100)    
print(lista_1_al_100[N])
print(lista_1_al_100.index(N))"""

"""9_ Genere un programa que pida cinco valores numéricos y los almacene en una lista a 
continuación pida un valor N su programa debe determinar si el valor N esta dentro de 
la lista y presentar por pantalla el mensaje correspondiente."""
"""
lista = []
i=1
while i <=5:
    n = int(input("Ingrese 5 numeros: "))
    lista.append(i)
    i+=1
N = int(input("Ingrese un numero a buscar: "))

if N in lista:
    print(f"La lista es de numeros ingresados es {lista} y el valor {N} SI se encuentra dentro de esta")
else:
    print(f"La lista es de numeros ingresados es {lista} y el valor {N} NO se encuentra dentro de esta")"""

"""26. Se tiene la lista de los apellidos de los alumnos de laboratorio IV: Albarado, Albornoz 
Gamboa, Barros, Blanca, Blanco, Bulacia, Cabral, Colombres Garmendia, Cortez, 
Cosiansi, Cura, Décima, Devani, Diaz, Dorado, Fernandez, Filsinger, Flores Gonzalez, 
Fresia, Gambarte Vera, Grande, Lacki Sinclairm, Lujan Weisheim, Montenegro 
Pastrana, Morales, Nieva Paratic, Peiro, Porro, Portillo Romero, Quinteros, Rey, 
Schujman, Soliz, Tabares, Urcan Lizondo, Williams Neme Scheij. Desarrolle un 
programa que pida que se introduzcan los apellidos como se ve en la lista y presente 
en pantalla cual es la bocal que mas se repite."""

""""i=1
apellidos =[]
vocales_que_estan=[]
while i <=2:
    nombres=str(input("ingrese 2 apellidos: "))
    apellidos.append(nombres)
    i+=1
veces_a,veces_e,veces_i,veces_o,veces_u = (0,0,0,0,0)

for apellido in apellidos:
    for letra in apellido:
        if letra == "a":
            veces_a+=1
        elif letra =="e":
            veces_e+=1
        elif letra == "i":
             veces_i+=1
        elif letra =="o":
            veces_o+=1
        elif letra =="u":
            veces_u+=1 

if veces_a>veces_e and veces_a>veces_i and veces_a>veces_o and veces_a>veces_u: 
    print("La vocal a es la que mas aparece")
elif veces_e>veces_a and veces_e>veces_i and veces_e>veces_o and veces_e>veces_u: 
    print("La vocal e es la que mas aparece")
elif veces_i>veces_a and veces_i>veces_e and veces_i>veces_o and veces_i>veces_u: 
    print("La vocal i es la que mas aparece")
elif veces_o>veces_a and veces_o>veces_e and veces_o>veces_i and veces_o>veces_u: 
    print("La vocal o es la que mas aparece")
elif veces_u>veces_a and veces_u>veces_e and veces_u>veces_i and veces_u>veces_o: 
    print("La vocal u es la que mas aparece")"""