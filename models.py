import csv, os
from config import *

def select_all(): # devolvera una lista con todos los registros de movimientos.csv
    fichero = open(MOVIMIENTOS_FILE,'r'   )
    csvReader = csv.reader(fichero, delimiter=",", quotechar='"')
    datos = []
    for item in csvReader:
        datos.append(item)
    fichero.close()
    #datos = [{'fecha':'18/12/2022','concepto': 'Regalo','cantidad':-276.00}, { 'fecha':'19/12/2022','concepto': 'Nomina', 'cantidad':1700}, {'fecha':'20/12/2022','concepto': 'Ropa','cantidad':-56.50} ]
    return datos


def select_by(id): # devolverá una registro con el id de la entrada
    mifichero = open(MOVIMIENTOS_FILE,'r')
    lectura = csv.reader(mifichero, delimiter=',', quotechar='"')
    registro_buscado = []
    for registro in lectura:
        if registro[0] ==str(id):
            registro_buscado = registro
    
    diccionario = dict()
    diccionario['id'] = registro_buscado[0]
    diccionario['date'] = registro_buscado[1]
    diccionario['concept'] = registro_buscado[2]
    diccionario['quantity'] = registro_buscado[3]
    mifichero.close()


    return registro_buscado

def delete_by(id): # borrara el registro cuyo id coinciden con el de la entrada del fichero
    fichero_old = open(MOVIMIENTOS_FILE,'r')
    fichero_new = open(MOVIMIENTOS_FILE_NEW,'w')

    csvReader = csv.reader(fichero_old, delimiter=",", quotechar='"')
    csvWriter = csv.writer(fichero_new, delimiter=",", quotechar='"')

    for registro in csvReader:
        if registro[0] != str(id):
            csvWriter.writerow(registro)
            
    
    fichero_old.close()
    fichero_new.close()

    os.remove(MOVIMIENTOS_FILE)
    os.rename(MOVIMIENTOS_FILE_NEW, MOVIMIENTOS_FILE)


def insert(registro_form): # crear nuevo registro compatible con el csv, asignando id unico y correlativo
    myFile= open(MOVIMIENTOS_FILE, 'a', newline='') #abrir archivo
    lectura = csv.writer(myFile, delimiter=",", quotechar='"') #creamos objeto lectura de csv para poder editar
    
    #crear id:
    fichero=open(LAST_ID_FILE, "r")
    registro = fichero.read()
    if registro == "":
        new_id = 1
    else:
        new_id = int(registro) + 1
    fichero.close()
    ficheroG = open(LAST_ID_FILE, "w")
    ficheroG.write(str(new_id))
    ficheroG.close()
        
    lectura.writerow([str(new_id)] + registro_form) #guarda los datos en el archivo.

    myFile.close()

def update_by(id, registro_modificado):
    pass
