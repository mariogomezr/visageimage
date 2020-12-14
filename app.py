from flask import Flask, render_template, redirect, request, flash
from flask.helpers import url_for
from flask_wtf import form
from forms import CambiaPassForm, LoginForm, OlvidaPassForm, RegistroForm
import sys
import logging


app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

#logging.basicConfig(filename='demo.log', level=logging.DEBUG)

class usuario():
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __init__(self, username, email):
        self.username = username
        self.email = email


# Variables dinamicas en el url = < string nombre > / <int id>  // con esto podemos sacar el id de la imagen y el usuario asociado a la imagen


prueba = { 
    'username' : 'magio',
    'password' : '1234'
}


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # Se instancia el objeto form --> WTForm
    if form.validate_on_submit():  # Se valida si el usuario envia un metodo POST con los datos validos
            usuario = form.usuario.data  # Con estos datos se valida en la BD si esta registrado
            contrasena = form.contrasena.data
            #app.logger.info( usuario + '------' + contrasena)  DEBUG
            if prueba['username'] == usuario and prueba['password'] == contrasena:
                #app.logger.info('ingreso sucessful')  DEBUG
                flash('Ingreso exitoso')
                return render_template("index.html")
            else: 
                flash('Intente de nuevo')
                #app.logger.info('Credenciales incorrectas') debug
    
    return render_template("ingreso.html", form=form)  # Solo es ejecuta en el metodo GET


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        usuario = form.usuario.data
        email = form.email.data
        contrasena = form.contrasena.data

        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render_template("registro.html", form=form)


@app.route('/olvidaPass', methods=['GET', 'POST'])
def olvidaPass():
    form = OlvidaPassForm()
    if form.validate_on_submit():
        email = form.email.data

        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render_template('olvidaPass.html', form=form)


@app.route('/cambiaPass', methods=['GET', 'POST'])
def cambiaPass():
    form = CambiaPassForm()
    if form.validate_on_submit():
        contrasena = form.contrasena.data
        confirmar = form.confirmar.data

        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render_template('cambiaPass.html', form=form)


@app.route('/nosotros', methods=['GET'])
def nosotros():
    return render_template('Nosotros.html')


@app.route('/vistaModificar', methods=['GET', 'POST'])
def vistaModificar():
    return render_template('vistaModificar.html')


# Dejar en POST para que cuando se inicie sesión se redireccione al perfil
@app.route('/perfil', methods=['GET', 'POST'])
def perfil():
    return render_template('perfil.html')


@app.route('/subirimagen', methods=['GET', 'POST'])
def subirimagen():
    return render_template('SubirImagen.html')


@app.route('/verImagen', methods=['GET'])
def verImagen():
    return render_template('verImagen.html')


@app.route('/terminos', methods=['GET'])
def terminos():
    return render_template('termsCond.html')


if __name__ == "__main__":
    app.run(debug=True)
