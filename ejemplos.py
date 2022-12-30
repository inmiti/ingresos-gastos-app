'''
# lectura de la primera línea del archivo:
with open ('data/movimientos.txt', "r") as resultado:
    leer = resultado.readline()
    print(leer)

# lectura de todo el contenido del archivo:
with open ('data/movimientos.txt', "r") as resultado1:
    leer1 = resultado1.read()
    print(leer1)

#otra manera:
result = open('data/movimientos.txt', "r")
lectura = result.read()
print(lectura)

result1 = open('data/movimientos.txt', "r")
lectura1 = result1.readlines()
print(lectura1)
'''
import csv

myFile= open('data/movimientos.txt', "r")
myFile = csv.reader(myFile, delimiter=",", quotechar=' " ')