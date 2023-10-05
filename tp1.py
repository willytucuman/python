#ejercicio1
#1. Ingrese tres números enteros, presentar por pantalla la suma y el promedio de estos.

#n1 = float(input("Ingrese el numero 1: "))
#n2 = float(input("Ingrese el numero 2: "))
#n3 = float(input("Ingrese el numero 3: "))
#suma = (n1 + n2 + n3)/3
#print(suma.__round__())

#2 Dado el radio de un círculo, presentar por pantalla el diámetro, perímetro y el área del círculo.
#radio = float(input("Coloque el radio del circulo: "))
#import math
#pi = math.pi
#diametro = float(radio *2)
#perimetro = float(2*pi*radio)
#area = float(pi * radio*radio)
#print("El valor del diametro es:",diametro.__round__(),".Su perimetro seria: ",perimetro.__round__(),"y su area: ",area.__round__())

#3  Escribir un programa que convierta una medida dada en metros a sus equivalentes en 
#decímetros, centímetros y milímetros. Presentar, por pantalla las cuatro magnitudes 
#con sus respectivas unidades.
#metros = float(input("Ingrese los metros que desea convertir: "))
#en_decimetros = metros/10
#en_centimetros = metros/100
#en_milimetros = metros/1000
#print("Tu unidad de medida que ingresaste en metros serian",en_decimetros,"decimetros, ",en_centimetros,"centimetros, ",en_milimetros,"milimetros")

#4 4. Dadas las tres notas trimestrales de un alumno en una respectiva materia en la 
#secundaria, presentar por pantalla si se exime, rinde en diciembre o rinde en marzo.
#n1 = float(input("Ingrese la primera nota del alumno: "))
#n2 = float(input("Ingrese la segunda nota del alumno: "))
#n3 = float(input("Ingrese la tercera nota del alumno: "))
#promedio = (n1+n2+n3)/3
#if promedio >= 5.51 :
 #   print("El alumno esta eximido")
#else :
 #   print("El alumno recupera en diciembre")

#5  Dada la fecha de nacimiento de una persona en el formato dd/mm/aaaa, devolver como resultado su edad en años

#diaN = int(input("Ingrese su dia de nacimiento: "))
#mesN = int(input("Ingrese su mes de nacimiento: "))
#añoN = int(input("Ingrese su año de nacimiento: "))

#diaA = int(input("Ingrese el dia actual: "))
#mesA = int(input("Ingrese el mes actual: "))
#añoA = int(input("Ingrese el año actual: "))
#edad = 0

#if diaA >= diaN and mesA >= mesN :
   # edad =  añoA - añoN
   # print("Su edad es: ",edad,"anos")
#elif diaA < diaN or mesA < mesN:
   # edad = ( añoA - añoN ) -1
    #print("Su edad es: ",edad,"anos")

#6  Dado un numero entero, determinar si el mismo es positivo, negativo o igual a cero.
#n =  int(input("Ingrese un numero entero porfavor: "))
#if  n > 0 :
 #   print(n," es mayor a cero")
#elif n == 0:
  #      print(n," es igual a cero")
#else:
 #         print(n," es menor a cero")

#7  Dado tres números enteros distintos, determinar si los mismo son consecutivos, sin importar el orden en que fueron ingresados.
#n1 = int(input("Ingrese el primer numero entero: "))
#n2 = int(input("Ingrese el segundo numero entero: "))
#n3 = int(input("Ingrese el tercero numero entero: "))
#if n1==n2-1 and n1 == n3-2:
 #   print("Ingreso 3 numeros consecutivos")
#elif n1==n3+2 and n1==n2+1:
 #   print("Ingreso 3 numeros consecutivos")
#elif n1==n2-1 and n3 == n2-2:
 #   print("Ingreso 3 numeros consecutivos")
#elif n2 == n1-2 and n3 ==n2+1:
 #   print("Ingreso 3 numeros consecutivos")
#elif n1 == n2 +1 and n3 == n2+2:
 #   print("Ingreso 3 numeros consecutivos")
#elif n1 == n2 - 2 and n3 == n1 +1:
 #   print("Ingreso 3 numeros consecutivos")
#else:
   # print("No ingreso numeros consecutivos") 
    
#8. Dado tres números enteros distintos, determinar si están ordenados en forma ascendente o descendente. Presentar por pantalla el mensaje correspondiente.
#n1 = int(input("Ingrese el primer numero entero: "))
#n2 = int(input("Ingrese el segundo numero entero: "))
#n3 = int(input("Ingrese el tercero numero entero: "))
#if n1<n2<n3:
 #   print("Puso numeros de manera ascendente")
#elif n1>n2>n3:
 #   print("Puso numeros de manera descendente")
#else:
    #print("no puso los numeros de manera ascendente o descendente")

#9 Ingresar tres números enteros distintos, ordenarlos de forma ascendente y presentarlos por pantalla.
#n1 = int(input("Ingrese el primer numero entero: "))
#n2 = int(input("Ingrese el segundo numero entero: "))
#n3 = int(input("Ingrese el tercero numero entero: "))

#if n1>n2>n3 :
 #   print(n3,n2,n1)
#elif n1>n3>n2:
 #   print(n2,n3,n1)
#elif n2>n1>n3:
 #  print(n3,n1,n2)
#elif n2>n3>n1:
 #   print(n1,n3,n2)
#elif n3>n1>n2:
 #   print(n2,n1,n3)
#elif n3>n2>n1:
    #print(n1,n2,n3)

#10 Dado un numero entero, determinar si es el mismo es par o impar
#n1 = int(input("Ingrese un numero entero: "))
#if n1 %2 ==0:
 #   print("El numero es par")
#else :
    #print("El numero es impar")    

#11  Dado dos números determinar si uno es múltiplo del otro
#n1 = int(input("Ingrese el primer numero entero: "))
#n2 = int(input("Ingrese el segundo numero entero: "))
#if n1%n2 ==0:
 #   print(n2," es multiplo de ",n1)
#elif n2%n1 ==0:
 #   print(n1," es multiplo de ",n2)
#else :
   # print("Los numeros no son multiplos entre si")

#12  Diseñar un algoritmo que presente por pantalla las 10 primeras tablas de multiplicar
#numeros_a_multiplicar = [1,2,3,4,5,6,7,8,9,10]
#tabla_del_1=[]
#tabla_del_2=[]
#tabla_del_3=[]
#tabla_del_4=[]
#tabla_del_5=[]
#tabla_del_6=[]
#tabla_del_7=[]
#tabla_del_8=[]
#tabla_del_9=[]
#tabla_del_10=[]
#i=1
#for i in numeros_a_multiplicar:
    #tabla_del_1.append(i*1)
    #tabla_del_2.append(i*2)
    #tabla_del_3.append(i*3)
    #tabla_del_4.append(i*4)
    #tabla_del_5.append(i*5)
    #tabla_del_6.append(i*6)
    #tabla_del_7.append(i*7)
   # tabla_del_8.append(i*8)
  #  tabla_del_9.append(i*9)
 #   tabla_del_10.append(i*10)
#print("tabla del 1: ",tabla_del_1)
#print("tabla del 2: ",tabla_del_2)
#print("tabla del 3: ",tabla_del_3)
#print("tabla del 4: ",tabla_del_4)
#print("tabla del 5: ",tabla_del_5)
#print("tabla del 6: ",tabla_del_6)
#print("tabla del 7: ",tabla_del_7)
#print("tabla del 8: ",tabla_del_8)
#print("tabla del 9: ",tabla_del_9)
#print("tabla del 10: ",tabla_del_10)

#13  Presentar por pantalla los N primeros números de la serie de Fibonacci
#def fibonacci(n):
    #fibonacci_sequence = []
    #a, b = 0, 1
    #for i in range(n):
        #fibonacci_sequence.append(a)
        #a, b = b, a + b
    #return fibonacci_sequence

# Solicitar al usuario el número de términos que desea ver
#n = int(input("Ingrese el número de términos de la serie de Fibonacci que desea generar: "))

#if n <= 0:
    #print("Por favor, ingrese un número positivo.")
#else:
    #resultado = fibonacci(n)
    #print("Los primeros", n, "números de la serie de Fibonacci son:")
    #print(resultado)

#14 Escribir un programa que presente por pantalla los números del 1 al 20
#i = 1
#lista=[]
#for i in range(1,21):
   #lista.append(i)
#print(lista)     

#15  Presentar por pantalla los N primeros números pares


