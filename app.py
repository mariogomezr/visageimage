from forms import CambiaPassForm, LoginForm, OlvidaPassForm, RegistroForm, subirimagenForm, ModificarForm, indexForm
from flask import Flask, render_template, flash, request, redirect, url_for, jsonify, session, send_file, current_app, g
from flask_mail import Mail, Message
from flask_wtf import form
import logging, email, sys, os, ntpath
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from db import get_db, close_db
import numpy as np

#Configuracion

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
app.config['UPLOAD_FOLDER'] = r'static\uploaded_img'
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



def login_required(view):
    def login_required_func():
        if g.user is None:      #no se ha logeado
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

def allowed_file(filename):         #Funcion que permite verificar las extensiones del archivo
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

           
#Funciones manejadoras

@app.route('/', methods=['GET', 'POST'])
def index():
    form = indexForm()
    varcontrol = 0
    if request.method == 'POST':
        form = indexForm()
        tag = form.tag.data
        lista = []
        db = get_db()
        imagenes_encontradas = db.execute('select tag, titulo, url from tag t join tag_img timg on t.id_tag = timg.fk_id_tag join imagenes img on img.pk_id_img = timg.fk_id_img where tag= ?', (tag,))
        for img in imagenes_encontradas:
            lista.append([img[0],img[1],img[2]])
        lista = np.array(lista)
        urls = set(lista[:,2])
        listaf = []
        for url in urls:
            valor = np.where(lista[:,2]==url)[0]
            string = ''
            titulo = lista[valor[0],1]
            for i in range(len(valor)):
                string = string + "#" + str(lista[valor[i],0]) + ' '
            listaf.append([url,titulo,string])
        return render_template('index.html', listaf= listaf, form = form, varcontrol = 1)

    else:
        db = get_db()
        if varcontrol == 1:
            lista = listaf
        else:
            lista = []
            for img in db.execute( 'select tag, titulo, url from tag t join tag_img timg on t.id_tag = timg.fk_id_tag join imagenes img on img.pk_id_img = timg.fk_id_img ORDER BY pk_id_img desc ' ):
                lista.append([img[0],img[1],img[2]])
            lista = np.array(lista)
            urls = set(lista[:,2])
            listaf = []
            for url in urls:
                valor = np.where(lista[:,2]==url)[0]
                string = ''
                titulo = lista[valor[0],1]
                for i in range(len(valor)):
                    string = string + "#" + str(lista[valor[i],0]) + ' '
                listaf.append([url,titulo,string])
            print(listaf)
        return render_template('index.html', listaf=listaf, form = form)

@app.route('/index-search')
def login_search(lista):
    db = get_db()

<<<<<<< HEAD
    for img in db.execute( 'select tag, titulo, url from tag t join tag_img timg on t.id_tag = timg.fk_id_tag join imagenes img on img.pk_id_img = timg.fk_id_img where privacidad = "publico" ' ):
        lista.append([img[0],img[1],img[2]])
=======
    for img in db.execute('select tag, titulo, url from tag t join tag_img timg on t.id_tag = timg.fk_id_tag join imagenes img on img.pk_id_img = timg.fk_id_img ORDER BY pk_id_img desc '):
        lista.append([img[0], img[1], img[2]])
>>>>>>> 85b63aeb817b8378f1b39ffce129acd501319ed6
    lista = np.array(lista)
    urls = set(lista[:, 2])
    listaf = []
    for url in urls:
        valor = np.where(lista[:, 2] == url)[0]
        string = ''
        titulo = lista[valor[0], 1]
        for i in range(len(valor)):
<<<<<<< HEAD
            string = string + "#" + str(lista[valor[i],0]) + ' '
        listaf.append([url,titulo,string])
=======
            string = string + "#" + str(lista[valor[i], 0]) + ' '
        listaf.append([url, titulo, string])
    print(listaf)
>>>>>>> 85b63aeb817b8378f1b39ffce129acd501319ed6

    return render_template('index-search.html', lista=listaf)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    
    form = LoginForm()
    if request.method == 'POST':
        db = get_db()
        form = LoginForm()  # Se instancia el objeto form --> WTForm
        if form.validate_on_submit():  # Se valida si el usuario envia un metodo POST con los datos validos
                usuario = form.usuario.data  # Con estos datos se valida en la BD si esta registrado
                contrasena = form.contrasena.data
                user = db.execute('SELECT * FROM usuarios WHERE username = ?', (usuario,)
                       ).fetchone()
                if user is None:    #Si el no se encuentra en la base de datos
                    error = 'Usuario o contrasena invalidos'
                    flash(error)
                    return render_template("ingreso.html", form=form)
                           #Si se encuentra, se crea la session y se devuelve a la pagina principal

                if check_password_hash(user['password'], contrasena):
                    session.clear()
                    session['user_id'] = user[0]
                    return redirect(url_for('index'))
                else:
                    error = 'Usuario o contrasena invalidos'
                    flash(error)
                    return render_template("ingreso.html", form=form)
        else:
            return render_template("ingreso.html", form=form)

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
            contrasena = generate_password_hash(form.contrasena.data)

            #Si el usuario ya existe
            if db.execute( 'SELECT id_usuario FROM usuarios WHERE username = ?', (usuario,) ).fetchone() is not None:
                error = 'El usuario {} ya existe'.format( usuario )
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
    flash('Se ha enviado un correo para cambiar tu contrasena')
    return redirect(url_for('login'))



@app.route('/cambiaPass', methods=['GET', 'POST'])
def cambiaPass():
    form = CambiaPassForm()
    if form.validate_on_submit():
        db = get_db()
        email = form.email.data
        contrasena = form.contrasena.data
        confirmar = form.confirmar.data

        db.execute(
            'UPDATE usuarios SET password = ? WHERE email = ?', (generate_password_hash(contrasena), email)
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

@login_required
@app.route('/modificar_imagen', methods=['GET', 'POST'])
def vistaModificar():
    form = ModificarForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            titulo = form.titulo.data
            url = form.url.data
<<<<<<< HEAD
            url = url.replace('http://127.0.0.1:5000/','').replace('/','\\')
            seleccion_privacidad = form.privacidad.data
            print(seleccion_privacidad)
=======
            url = url.replace('http://127.0.0.1:5000/','').replace('https://54.91.130.114/', '').replace('/','\\')
>>>>>>> 85b63aeb817b8378f1b39ffce129acd501319ed6
            db = get_db()
            id = db.execute("select pk_id_img from imagenes where url=?",((url),)).fetchone()
            ide = id[0]
            if request.form['btn_actualizar'] == 'Actualizar':  #Si se presiona el boton de actualizar
                archivo = request.files['file']
                if archivo is None or archivo.filename == '':
                    db.execute('UPDATE imagenes SET url = ? , titulo = ? ,  privacidad= ?  WHERE pk_id_img = ?',(url,titulo,seleccion_privacidad,ide) )
                    db.commit()
                    return redirect(url_for('perfil'))

                if archivo and allowed_file(archivo.filename):   #Si existe el archivo y tiene extension permitida
                    archivo_seguro = secure_filename(archivo.filename)
                    path_archivo = os.path.join(app.config['UPLOAD_FOLDER'], archivo_seguro)
                    
                    #Si la imagen ya existe en la BD
                    if db.execute( 'SELECT url FROM imagenes WHERE url = ?', (path_archivo,) ).fetchone() is not None:
                        error = 'La imagen ya existe en la base de datos, pruebe con un nombre diferente'
                        flash( error )
                        return redirect(url_for('perfil'))
                    else:
                        ruta = os.path.join(app.config['UPLOAD_FOLDER'],archivo.filename)
                        archivo.save(os.path.join(app.config['UPLOAD_FOLDER'],archivo.filename))   #Se graba en la carpeta
                        db.execute('UPDATE imagenes SET url = ? , titulo = ? WHERE pk_id_img = ?',(ruta,titulo,ide) )
                        db.commit()
                        return redirect(url_for('perfil'))

            if request.form['btn_actualizar'] == 'Eliminar':      #si se presiona el boton de eliminar
                db.execute('delete from tag_img where fk_id_img = ?',((int(ide)),))
                db.commit()
                db.execute('delete from imagenes where pk_id_img = ?',((int(ide)),))
                db.commit()
                return redirect(url_for('perfil'))
            
    return render_template('vistaModificar.html', form = form)


# Dejar en POST para que cuando se inicie sesión se redireccione al perfil
@login_required
@app.route('/perfil', methods=['GET', 'POST'])
def perfil():
    db = get_db()
    nombreUsuario = g.user[1]
    lista = []

    for img in db.execute( 'select tag, titulo, url from tag t join tag_img timg on t.id_tag = timg.fk_id_tag join imagenes img on img.pk_id_img = timg.fk_id_img where autor = ?', (str(nombreUsuario),) ):
        lista.append([img[0],img[1],img[2]])
    lista = np.array(lista)
    urls = set(lista[:,2])
    listaf = []
    for url in urls:
        valor = np.where(lista[:,2]==url)[0]
        string = ''
        titulo = lista[valor[0],1]
        for i in range(len(valor)):
            string = string + str(lista[valor[i],0]) + ' '
        listaf.append([url,titulo,string])

    return render_template('perfil.html', listaf=listaf, nombreUsuario=nombreUsuario)


@login_required
@app.route('/subirimagen', methods=['GET', 'POST'])
def subirimagen():
    form = subirimagenForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            usuario = g.user[1]            #Nombre del usuario en la session
            titulo_img = form.titulo_img.data
            etiq_img = form.etiq_img.data.split()  #split por espacio ETIQUETAS
            archivo = request.files['file']
            db = get_db()

            if archivo is None or archivo == '':
                flash('Ingrese un archivo con extension .jpg o .png')
                return render_template('subirimagen.html', form = form)

            if archivo and allowed_file(archivo.filename):   #Si existe el archivo y tiene extension permitida
                archivo_seguro = secure_filename(archivo.filename)
                path_archivo = os.path.join(app.config['UPLOAD_FOLDER'], archivo_seguro)
                
                #Si la imagen ya existe en la BD
                if db.execute( 'SELECT url FROM imagenes WHERE url = ?', (path_archivo,) ).fetchone() is not None:
                    error = 'La imagen ya existe en la base de datos, pruebe con un nombre diferente'
                    flash( error )
                    return render_template( 'subirimagen.html', form=form)
                else:
                    seleccion_privacidad = form.privacidad.data
                    print(seleccion_privacidad)
                    archivo.save(os.path.join(app.config['UPLOAD_FOLDER'],archivo.filename))   #Se graba en la carpeta
                    db.execute(     #Ejecucion del query
                    'INSERT INTO imagenes (url, autor, titulo, fk_usuario, privacidad) VALUES (?,?,?,?,?)',
                    (path_archivo, usuario, titulo_img, usuario, seleccion_privacidad) )
                    db.commit()     #Chequear informacion en la BD

                     #Metodo para subir las etiquetas
                    id_img = db.execute('SELECT pk_id_img FROM IMAGENES  WHERE URL = ?', (path_archivo,)).fetchone()[0]  #extraer el id img de
                    for etiqueta in etiq_img:           #por cada etiqueta
                        if  db.execute('SELECT * FROM tag WHERE tag = ?', (etiqueta,)).fetchone() is None: #chequeo que la etiqueta no exista
                            db.execute('INSERT INTO tag(tag) VALUES (?)', (etiqueta,))    
                            db.commit()                       #se crea la etiqueta
                        etiq = db.execute('SELECT id_tag from tag where tag = ?',(etiqueta,)).fetchone()[0]   #'id_tag': valor
                        db.execute('INSERT INTO tag_img(fk_id_img, fk_id_tag) values (?,?)', (id_img, etiq))        #Se agregan los datos a tag_img
                        db.commit() 

                    return redirect(url_for('perfil'))  
               

    return render_template('SubirImagen.html', form = form)

@app.route( '/downloadimage', methods=['GET', 'POST'] )
@login_required
def download_image(file_url):
    return send_file( file_url, as_attachment=True )

@app.route('/verImagen', methods=['GET'])
def verImagen():
    nombreUsuario = g.user[1]
    return render_template('verImagen.html', nombreUsuario=nombreUsuario)


@app.route('/terminos', methods=['GET'])
def terminos():
    return render_template('termsCond.html')



if __name__ == "__main__":
    app.run(host= '127.0.0.1', port=443, ssl_context=('cert.pem','key.pem'))
