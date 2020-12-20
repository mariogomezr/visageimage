from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, FileField
from wtforms import validators
from wtforms.validators import DataRequired, Email, EqualTo, Length


class LoginForm (FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(), Length(max=64)])
    contrasena = PasswordField('Contraseña ', validators=[DataRequired(), ])
    submit = SubmitField('Iniciar sesión')

class ModificarForm (FlaskForm):
    titulo = StringField('', validators=[DataRequired(), Length(max=64)])
    etiquetas = StringField('', validators=[DataRequired(), ])
    file = FileField('file')
    submit_actualizar = SubmitField('Actualizar')
    submit_eliminar = SubmitField('Eliminar')


class RegistroForm(FlaskForm):
    nombre = StringField('Nombre completo', validators=[DataRequired(), Length(max=64)])
    usuario = StringField('Usuario', validators=[DataRequired(), Length(max=64)])
    email = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    contrasena = PasswordField('Contraseña ', validators=[DataRequired()])
    submit = SubmitField('Registrarse')


class OlvidaPassForm(FlaskForm):
    email = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    submit = SubmitField('Enviar')


class CambiaPassForm(FlaskForm):
    email = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    contrasena = PasswordField('Nueva contraseña', validators=[DataRequired(), EqualTo('confirmar', message='Las contraseñas deben coincidir')])
    confirmar = PasswordField('Repite la contraseña', validators=[DataRequired()])
    submit = SubmitField('Cambiar')

class subirimagenForm(FlaskForm):
    titulo_img = StringField('tituloImagen',validators=[DataRequired()])
    etiq_img = StringField('etiqueta',validators=[DataRequired()])
    file = FileField('file' )
    submit = SubmitField('Guardar')