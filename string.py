#multiline strings assigned to a variable with three doube quotes
a = """ 
    Hola mi nombre es tomas williams,
    tengo 22 anos,
    peleo mma amateur.
"""
#print(a)

#multiline strings assigned to a variable with three simple quotes
x = '''
 Hola mi nombre es tomas williams,
    tengo 22 anos,
    peleo mma amateur.
'''
#print(x)

#strings as arrays
b = "Hola mi nombre es tomas"
#print(b[1])

#loop in string
z = "banana"
#for i in z :
 #   print(i)

#checking in strings
#we can use for check if a string is into another string with in sentence and too we can check if is not into another string with NOT IN sentence

#sentence in
a = "En argentina todo esta muy caro"
#print("caro" in a) #seria true

#sentence not in
a = "En argentina todo es muy barato"
#print("barato" not in a) #seria false

#slicing strings
#print(a[4:7])

#negative indexing
#print(a[-5:-2]) el resultado es ara, se cuenta desde el -1 de derecha a izquierda

#methods for modify strings
#remove whitespaces before or after the string, not whitespaces that are inside string
a=" Hello, world!,i'm the champion {}"
#print(a.strip())

#replace string
#print(a.replace("H","J")) reemplazo la h por la j

#print(a.split(",")) la coma como argumento en realidad detecta por cada cuanto el split separara e insertara como elemnto dentro de la string que devolvera

#format method
b = "Hello i'm tomas and age {}"
n = 32
#print(b.format(n))

#escape character
f = "Yo tengo \"200\" amigos \n y ella"
#print(f)

#casting nos permite definir en que tipo de dato queremos que sea la variable
x=int(20.8)
#aca queremos que por mas que sea flotante se exprese como entero
#print(bool(True))


#Este ejemplo es otra forma de la cual devuelve false
#class miclase():
    #def __len__(self):
     #   return 0
#miobjeto=miclase()
#print(bool(miobjeto))

#negative print indexes
#lista = ["dasdsa","sadsad","fdffd",234,{"dsdsa":"sdasd"}]
#print(lista[-5:-3])

#probando que pasa si pongo un rango que es de menos o de mas
#lista = ["manzana","banana","pera","mango"]
#lista[0:2]=["sandia","melon"]
#print(lista.__len__())
#print(lista)

#insert items
#lista = ["manzana","banana","pera","mango"]
#lista.insert(1,"uva")
#print(lista)
#print(lista.__len__())

#agregando una tupla un array
#thislist = ["apple", "banana", "cherry"]
#thistuple = ("kiwi", "orange")
#thislist.extend(thistuple)
#print(thistuple)

#'''estamos recorriendo y escribiendo cada uno de los items pero con range que toma la longitud de la lista y 
# a la hora de escribir el iterable que es i
# '''
#lista = [1,2,3,4]
#for i in range(len(lista)):
    #print(lista[i])

#recorriendo con un while loop
#lista = [1,2,3,4]
#i=0
#while i<lista.__len__() :
    #print(lista[i])
    #i+=1

#list comprenhension
#frutas = ["manzana","oso","libro","mango"]
#frutas_con_a = [x if x!="oso" else "naranja" for x in frutas] 
#print(frutas_con_a)

      