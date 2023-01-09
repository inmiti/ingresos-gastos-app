from app_registro import app
from flask import render_template, request, redirect
import csv
import os
from datetime import date, datetime
from config import *
from models import *

@app.route("/")
def index():
    datos = select_all()
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
            insert([request.form['date'],
            request.form['concept'], 
            request.form['quantity']]) #guarda los datos en el archivo.

    return redirect('/')


@app.route("/update/<int:id>", methods= ['GET', 'POST'])
def edit(id):
    if request.method == 'GET':

        registro = select_by(id)
        return render_template("update.html", pageTitle = "Modificar", typeAction = "modificar", butonAction = "Editar", dataForm =registro)
    else:
        pass

@app.route("/delete/<int:id>", methods = ["GET", "POST"])
def remove(id):
    if request.method == "GET":
        
        registro_buscado = select_by(id)
        
        if len(registro_buscado) > 0: #en el caso de que no encontrar el registro len =0, redirecciona a index
            return render_template("delete.html", pageTitle = "Eliminar", registros = registro_buscado)
        else:
            return redirect("/")
    else:
        delete_by(id)
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