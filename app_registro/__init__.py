from flask import Flask

app = Flask(__name__) #inicializa la app con __name__ es main.py en este caso, ya que hacemos export FLASK_APP = main.py y lask --app main --debug run
from app_registro.routes_v1 import * #hay que referenciar las ruts debajo de app:


# para inicializar el servidor de flask en mac:  export FLASK_APP = main.py en el terminal

# flask --app main --debug run se hace en el terminal para qque ejecute en modo debug, se va actualizando solo el codigo qque vamos creando.
# otra alternativa a lo anterior es crear un archivo oculto y agregar las lines: FLASK_APP = main.py  // FLASK_DEBUG = true.