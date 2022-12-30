from app_registro import app
from flask import render_template
import csv

@app.route("/")
def index():
    fichero = open('data/movimientos.txt',"r")
    csvReader = csv.reader(fichero, delimiter=",", quotechar='"')
    datos = []
    for item in csvReader:
        datos.append(item)
    
    #datos = [{'fecha':'18/12/2022','concepto': 'Regalo','cantidad':-276.00}, { 'fecha':'19/12/2022','concepto': 'Nomina', 'cantidad':1700}, {'fecha':'20/12/2022','concepto': 'Ropa','cantidad':-56.50} ]
    return render_template("index.html", pageTitle = "Listas", lista = datos)

@app.route("/new", methods =['GET', 'POST'])
def create():
    return render_template("new.html", pageTitle = "Nuevo", typeAction = "alta", butonAction = "Guardar")


@app.route("/update")
def edit():
    return render_template("update.html", pageTitle = "Modificar", typeAction = "modificar", butonAction = "Editar")

@app.route("/delete")
def remove():
    return render_template("delete.html", pageTitle = "Borrar", typeAction = "borrar", butonAction = "Guardar")