from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    astronaut_id = StringField('ID асторнавта', validators=[DataRequired()])
    astronaut_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    capitan_id = StringField('ID капитана', validators=[DataRequired()])
    capitan_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Войти')
