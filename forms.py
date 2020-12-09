from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length

class LoginForm (FlaskForm):
    usuario = StringField('Usuario', validators = [DataRequired(), Length(max = 64)] )
    contrasena = PasswordField('Contraseña ', validators = [DataRequired(), ] )
    submit = SubmitField('Iniciar sesión')  #render_kw={"onclick": "{{ url_for('registro') }}"  esto sirve para darle una funcion cuando de click al boton
    submit2 = 

