from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length,EqualTo


class FormCriarCategoria(FlaskForm):
    nome = StringField('Nome',validators=[DataRequired(), Length(0,60)])
    submit_categoria = SubmitField('Criar Categoria')