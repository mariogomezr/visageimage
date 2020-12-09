from flask import Flask, render_template, redirect, request, flash
from forms import LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

# Variables dinamicas en el url = < string nombre > / <int id>  // con esto podemos sacar el id de la imagen y el usuario asociado a la imagen


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()                  #Se instancia el objeto form --> WTForm
    if form.validate_on_submit():       #Se valida si el usuario envia un metodo POST con los datos validos
        if form.submit.data:
            usuario = form.usuario.data         #Con estos datos se valida en la BD si esta registrado
            contrasena = form.contrasena.data
            #FALTA funcion chequear que el usuario este en la BD
        
        #next = request.args.get('next', None)   #Si lo esta tal accion
        #if next:
        #    return redirect(next)
        return render_template("index.html")    #sino esta accion
    return render_template("ingreso.html", form = form) # Solo es ejecuta en el metodo GET


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


if __name__ == "__main__":
    app.run(debug=True)
