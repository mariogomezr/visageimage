from flask import Flask, render_template


app = Flask(__name__)

# Variables dinamicas en el url = < string nombre > / <int id>  // con esto podemos sacar el id de la imagen y el usuario asociado a la imagen


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('ingreso.html')


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    return render_template('registro.html')


@app.route('/cambiaPass', methods=['GET', 'POST'])
def cambiaPass():
    return render_template('cambiaPass.html')


@app.route('/nosotros', methods=['GET'])
def nosotros():
    return render_template('Nosotros.html')


@app.route('/perfil', methods=['GET', 'POST'])  # Dejar en POST para que cuando se inicie sesión se redireccione al perfil
def perfil():
    
    return render_template('perfil.html')

@app.route('/subirimagen', methods=['GET','POST'])
def subirimagen():
    return render_template('SubirImagen.html')

if __name__ == "__main__":
    app.run(debug=True)
