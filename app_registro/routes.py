from app_registro import app
from flask import render_template

@app.route("/")
def index():
    datos = [{'fecha':'18/12/2022','concepto': 'Regalo','cantidad':-276.00}, { 'fecha':'19/12/2022','concepto': 'Nomina', 'cantidad':1700}, {'fecha':'20/12/2022','concepto': 'Ropa','cantidad':-56.50} ]
    return render_template("index.html", pageTitle = "Listas", lista = datos)

@app.route("/new")
def create():
    return render_template("new.html", pageTitle = "Nuevo")


@app.route("/update")
def edit():
    return render_template("update.html", pageTitle = "Modificar")

@app.route("/delete")
def remove():
    return render_template("delete.html", pageTitle = "Borrar")