from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms import validators
from wtforms.validators import DataRequired, Email, EqualTo, Length


class LoginForm (FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(), Length(max=64)])
    contrasena = PasswordField('Contraseña ', validators=[DataRequired(), ])
    # render_kw={"onclick": "{{ url_for('registro') }}"  esto sirve para darle una funcion cuando de click al boton
    submit = SubmitField('Iniciar sesión')


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
    contrasena = PasswordField('Nueva contraseña', validators=[DataRequired(), EqualTo('confirmar', message='Las contraseñas deben coincidir')])
    confirmar = PasswordField('Repite la contraseña', validators=[DataRequired()])
    submit = SubmitField('Cambiar')