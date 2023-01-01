from app_registro import app
from flask import render_template, request, redirect
import csv
from datetime import date, datetime

@app.route("/")
def index():
    fichero = open('data/movimientos.csv','r'   )
    csvReader = csv.reader(fichero, delimiter=",", quotechar='"')
    datos = []
    for item in csvReader:
        datos.append(item)
    
    #datos = [{'fecha':'18/12/2022','concepto': 'Regalo','cantidad':-276.00}, { 'fecha':'19/12/2022','concepto': 'Nomina', 'cantidad':1700}, {'fecha':'20/12/2022','concepto': 'Ropa','cantidad':-56.50} ]
    return render_template("index.html", pageTitle = "Listas", lista = datos)

@app.route("/new", methods =['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template("new.html", pageTitle = "Nuevo", typeAction = "alta", butonAction = "Guardar")
    else:
        myFile= open('data/movimientos.csv', 'a', newline='') #abrir archivo
        lectura = csv.writer(myFile, delimiter=",", quotechar='"') #creamos objeto lectura de csv para poder editar
        
        #fechaFormat =datetime.strptime(request.form['date'], '%Y-%m-%d') #formatear fecha para que se pase al formato aaaa-mm-dd. hay qque hacer .date() para pasar a class datetime.date, para poder comparar luego con date.today()
        #requerimos que la fecha introducida sea inferior o igual al día de hoy:
        
        hoy = date.today().isoformat() #iso format pasa la class date a str
        
        if request.form['date'] > hoy:
            return render_template("new.html", pageTitle = "Nuevo", typeAction = "alta", butonAction = "Guardar")
        else:
            lectura.writerow([request.form['date'],request.form['concept'], request.form['quantity']]) #guarda los datos en el archivo.
            myFile.close()

    return redirect('/')


@app.route("/update")
def edit():
    return render_template("update.html", pageTitle = "Modificar", typeAction = "modificar", butonAction = "Editar")

@app.route("/delete")
def remove():
    return render_template("delete.html", pageTitle = "Borrar", typeAction = "borrar", butonAction = "Guardar")



def validateForm():
    pass