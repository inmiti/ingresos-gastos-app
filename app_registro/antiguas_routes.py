from app_registro import app
from flask import render_template, request, redirect
import csv
import os
from datetime import date, datetime
from config import *
from models import *

@app.route("/")
def index():
    fichero = open(MOVIMIENTOS_FILE,'r'   )
    csvReader = csv.reader(fichero, delimiter=",", quotechar='"')
    datos = []
    for item in csvReader:
        datos.append(item)
    fichero.close()
    #datos = [{'fecha':'18/12/2022','concepto': 'Regalo','cantidad':-276.00}, { 'fecha':'19/12/2022','concepto': 'Nomina', 'cantidad':1700}, {'fecha':'20/12/2022','concepto': 'Ropa','cantidad':-56.50} ]
    
    return render_template("index.html", pageTitle = "Listas", lista = datos)

@app.route("/new", methods =['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template("new.html", pageTitle = "Nuevo", typeAction = "alta", butonAction = "Guardar", dataForm = {})
    else:
        error = validateForm(request.form)
        
        if error: 
            return render_template("new.html", pageTitle = "Nuevo", typeAction = "alta", butonAction = "Guardar", msError = error, dataForm = request.form)
        else:
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
             
            lectura.writerow([new_id,request.form['date'],request.form['concept'], request.form['quantity']]) #guarda los datos en el archivo.
        
        myFile.close()

    return redirect('/')


@app.route("/update/<int:id>")
def edit(id):
    return render_template("update.html", pageTitle = "Modificar", typeAction = "modificar", butonAction = "Editar")

@app.route("/delete/<int:id>", methods = ["GET", "POST"])
def remove(id):
    if request.method == "GET":
        mifichero = open(MOVIMIENTOS_FILE,'r')
        lectura = csv.reader(mifichero, delimiter=',', quotechar='"')
        registro_buscado = []
        for registro in lectura:
            if registro[0] ==str(id):
                registro_buscado = registro
        mifichero.close()
        if len(registro_buscado) > 0: #en el caso de que no encontrar el registro len =0, redirecciona a index
            return render_template("delete.html", pageTitle = "Eliminar", registros = registro_buscado)
        else:
            return redirect("/")
    else:
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
        return redirect("/")

def validateForm(requestForm):
    hoy = date.today().isoformat() #iso format pasa la class date a str
    errores = []
    if requestForm['date'] > hoy:
        errores.append("fecha inválida: La fecha ha de ser igual o anterior al día de hoy")
    if requestForm['concept'] == "":
        errores.append("concepto vacío: Introduce un concepto para registrar el ingreso o gasto")
    if requestForm['quantity'] == "" or float(requestForm['quantity']) ==0.0:
        errores.append("cantidad vacío o cero: Introduce una cantidad positiva para ingresos y negativa para gastos")
    return errores