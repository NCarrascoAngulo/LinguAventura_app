from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
  username = StringField('Nombre de usuario', 
                         validators=[DataRequired(), Length(min=2, max=30)])
  email = StringField('Email',
                      validators=[DataRequired(), Email()])
  password = PasswordField('Contraseña', validators=[DataRequired()])
  confirm_password = PasswordField('Confirma contraseña',
                      validators=[DataRequired(), EqualTo('password')])                                
  submit = SubmitField('Incríbete')

class LoginForm(FlaskForm):
  email = StringField('Email',
                      validators=[DataRequired(), Email()])
  password = PasswordField('Contraseña', validators=[DataRequired()])
  remember = BooleanField('Recuérdamelo')
  submit = SubmitField('Acceso') 
