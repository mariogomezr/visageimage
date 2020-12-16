from forms import CambiaPassForm, LoginForm, OlvidaPassForm, RegistroForm
from flask import Flask, render_template, flash, request, redirect, url_for, jsonify, session, send_file, current_app, g
from flask_mail import Mail, Message
from flask_wtf import form
import logging, email, sys
from db import get_db, close_db

#Configuracion
app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'visageimage01@gmail.com',
    MAIL_PASSWORD = 'misiontic123'
)
mail = Mail(app)


#Funciones decoradoras
@app.before_request
def load_logged_in_user():
    user_id = session.get( 'user_id' )

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM usuarios WHERE id_usuario = ?', (user_id,)
        ).fetchone()

def login_required():
    def login_required_func():
        if g.user is None:
            return redirect( url_for( 'login' ) )
    return login_required_func

#Helper Functions

def enviar_mensaje_activacion(email=None):
    msg = mail.send_message(
        'Activar cuenta',
        sender = 'VisageImage',
        recipients = [email],
        body = 'Ingresa al siguiente link para activar tu cuenta: {}'.format(url_for('index'))
    )
    return 'Mensaje enviado'

#Funciones manejadoras

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        db = get_db()
        form = LoginForm()  # Se instancia el objeto form --> WTForm
        if form.validate_on_submit():  # Se valida si el usuario envia un metodo POST con los datos validos
                usuario = form.usuario.data  # Con estos datos se valida en la BD si esta registrado
                contrasena = form.contrasena.data
                user = db.execute('SELECT * FROM usuarios WHERE username = ? AND password = ?', (usuario, contrasena)
                       ).fetchone()
                if user is None:    #Si el no se encuentra en la base de datos
                    error = 'Usuario o contrasena invalidos'
                    flash(error)
                    return render_template("ingreso.html", form=form)
                else:               #Si se encuentra, se crea la session y se devuelve a la pagina principal
                    session.clear()
                    session['user_id'] = user[0]
                    return redirect( url_for('index'))

    if request.method == 'GET':
        return render_template("ingreso.html", form=form)  # Solo es ejecuta en el metodo GET


@app.route( '/logout' )
def logout():
    session.clear()
    return redirect( url_for( 'index' ) )

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistroForm()
    if request.method == 'POST':
        form = RegistroForm()
        if form.validate_on_submit():
            db = get_db()
            nombre = form.nombre.data
            usuario = form.usuario.data
            email = form.email.data
            contrasena = form.contrasena.data

            #Si el usuario ya existe
            if db.execute( 'SELECT id_usuario FROM usuarios WHERE username = ?', (usuario,) ).fetchone() is not None:
                error = 'El correo {} ya existe'.format( usuario )
                flash( error )
                return render_template( 'registro.html', form=form)

            #Si el correo ya existe
            if db.execute( 'SELECT id_usuario FROM usuarios WHERE email = ?', (email,) ).fetchone() is not None:
                error = 'El correo {} ya existe'.format( email )
                flash( error )
                return render_template( 'registro.html', form=form)

            db.execute(     #Ejecucion del query
                'INSERT INTO usuarios (username, email, password, name) VALUES (?,?,?,?)',
                (usuario, email, contrasena, nombre)
            )
            db.commit()     #Chequear informacion en la BD
            flash( 'Revisa tu correo para activar tu cuenta' )
            enviar_mensaje_activacion(email=email)
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
        return redirect(url_for('enviar_mensaje', email=email))
    return render_template('olvidaPass.html', form=form)


@app.route('/mensaje/<string:email>')
def enviar_mensaje(email=None):
    msg = mail.send_message(
        'Cambiar contraseña',
        sender = 'VisageImage',
        recipients = [email],
        body = 'Ingresa al siguiente link para restablecer tu contraseña: http://127.0.0.1:5000/cambiaPass'
    )
    return 'Mensaje enviado'



@app.route('/cambiaPass', methods=['GET', 'POST'])
def cambiaPass():
    form = CambiaPassForm()
    if form.validate_on_submit():
        db = get_db()
        email = form.email.data
        contrasena = form.contrasena.data
        confirmar = form.confirmar.data

        db.execute(
            'UPDATE usuarios SET password = ? WHERE email = ?', (contrasena, email)
        )
        db.commit()

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
