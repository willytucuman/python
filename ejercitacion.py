#n1 =  int(input("Dame el primer numero positivo: "))
#n2 = int(input("Dame el segundo numero positivo: "))

#if n1==n2:
    #print("No hay suma entre ellos por ser iguales")
#elif n2<n1:
    #auxiliar = n2
    #n2 = n1
    #n1 = auxiliar
    
#i = 0
#N = n1+1

#while N< n2:    
    #i = i+N
   # N+=1

#print(i)

#numeros primos
#N= int(input("Deme un numero entero positivo: "))
#N2 = N-1

#while 1<N2 and N%N2!=0:
 #   N2-=1  

#if N2 ==1 or N ==1:
    #print("El numero es primo")
#else :
    #print("No es primo")

#suma de numeros primos comprendidos entre dos numeros 
"""N1= int(input("Deme un primer numero entero positivo: "))
N2= int(input("Deme un segundo numero entero positivo: "))

N = N1+1
Sum = 0

while N<N2:
    D = N1-1
    while 1<D and N2%D !=0:
        D -=1
    if D ==1 or N==1:
        Sum+=N
    N+=1

if Sum==0:
    print("No hay numeros primos comprendidos")
else:
    print(f"La suma de estos es:{Sum}")"""

#metodos de set
set1 = {"banana","manzana","pera"}
set2 = {"melon","sandia","banana"}
#agregar un elemento a cualquiera
"""set1.add("uva")
print(set1)"""
#limpiando un set
"""set1.clear()
print(set1)"""
#copiando un set en otro
"""set3 = set1.copy()
print(set3)"""
#DIFERENCIAS
"""set3 = set2.difference(set1)
print(set3)"""
#interseccion
"""set3 = set1.intersection(set2)
print(set3)"""
#INDICAMOS SI UNO ES SUBSET DE OTRO
"""set3 = set1.issubset(set2)
print(set3)"""
#