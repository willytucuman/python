#creando un diccionario
alumno ={
    "nombre":"tomas",
    "edad":22,
    "carrera": "TUP",
    "Deporte":"mma"
}
#trayendo un item por su key 
"""print(alumno["nombre"])"""

#longitud del diccionario
"""print(len(alumno))"""
#trayendo las key de mi diccionario
"""x = alumno.keys()
print(x)"""
#agregando una key que no existia
"""alumno["hobbie"] = "comer rico"
print(x)"""
#trayendo los items
"""x  = alumno.items()
print(x)"""
#update method
"""alumno.update({"nombre":"marcos"})
print(alumno)"""
#agregando con update
""""alumno.update({"premium":False}) agregando algo que no existe con update"""
#eliminando con pop 
"""alumno.pop("nombre") sino pasamos nada se elimina el ultimo item
print(alumno)"""
#deleteando un item
"""del alumno["nombre"] aca borramos un item
del alumno aca borramos todo el diccionario"""
#navegando por el diccionario
"""for x in alumno:
    print(x) aca traemos las keys
for x in alumno:
    print(alumno[x]) aca traemos los values"""
#trayendo keys y values con metodos
"""for x in alumno.values():
    print(x)
for x in alumno.keys():
    print(X)"""  
#trayendo key y values
"""for x,y in alumno.items():
    print(x,':',y)"""
#anidando diccionarios
"""alumno2 = alumno.copy()
alumnos = {"primer alumno":alumno,"segundo alumno":alumno2}
print(alumnos)"""
#diccionario que contiene diccionarios
"""diccionario = {"primed diccioario":{'cosa1':1,"cosa2":2},
               "segundo diccionario":{'cosa1':1,"cosa2":2},
               "tercer diccionario":{'cosa1':1,"cosa2":2}}
print(diccionario)"""
