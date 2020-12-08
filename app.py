
from flask import Flask, render_template


app = Flask(__name__)

#Variables dinamicas en el url = < string nombre > / <int id>  // con esto podemos sacar el id de la imagen y el usuario asociado a la imagen

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods = ['GET'])
def login():
    return render_template('ingreso.html')

@app.route('/registro', methods = ['GET', 'POST'])
def registro():
    return render_template('registro.html')


@app.route('/nosotros', methods = ['GET'])
def nosotros():
    return render_template('Nosotros.html')

@app.route('/perfil', methods = ['GET'])
def perfil():
    return render_template('perfil.html')


if __name__ == "__main__":
    app.run(debug = True)