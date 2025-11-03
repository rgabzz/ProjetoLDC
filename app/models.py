
# Banco de Dados
from . import db
from flask_login import UserMixin
from sqlalchemy import Integer,String,DateTime,ForeignKey,Text,Numeric,Enum

class Usuarios(UserMixin,db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(Integer,primary_key=True)
    nome = db.Column(String(120), nullable=False) 
    email = db.Column(String(255), nullable=False,unique=True) 
    senha_hash = db.Column(String(255), nullable=False)
    criado_em = db.Column(DateTime(),default=db.func.now())
    cargo = db.Column(Enum('membro','admin', name='cargo'),default='membro')

    def __repr__(self):
        return f'<Usuario: {self.nome}>'
    
class Listas(db.Model):
    __tablename__ = 'listas'

    id = db.Column(Integer,primary_key=True)
    usuario_id = db.Column(Integer, ForeignKey('usuarios.id', ondelete='CASCADE') ,nullable=False)
    titulo = db.Column(String(200), nullable=False)
    data_criada = db.Column(DateTime(),default=db.func.now())
    data_ultima_atualizacao = db.Column(DateTime(),default=db.func.now(),onupdate=db.func.now())

    usuario = db.relationship('Usuarios', backref=db.backref('listas', passive_deletes=True))

    '''
        db.relationship('Usuario') -> Cria uma relação dessa tabela com a outra, podendo pesquisar o dono 
        de uma tabela pela outra.
         - print(lista.usuario.username)

        backref=db.backref('listas', passive_deletes=True) -> Cria um atributo que permite ver as listas de um usuário pela tabela de Usuario e o passive_deletes garante q o sql_alchemy não tente deletar uma linha da tabela sozinha, que o proprio banco vai cuidar disso.
        - usuario.listas
    '''

    def __repr__(self):
        return f'<Lista: {self.titulo}>'
    
class Categorias(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(Integer,primary_key=True) 
    nome = db.Column(String(60),nullable=False,unique=True)
    criado_em = db.Column(DateTime(),default=db.func.now())


    def __repr__(self):
        return f'<Categoria: {self.nome}>'
    
class Itens(db.Model):
    __tablename__ = 'itens'

    id = db.Column(Integer,primary_key=True)
    lista_id = db.Column(Integer, ForeignKey('listas.id', ondelete='CASCADE') ,nullable=False)
    nome = db.Column(String(200),nullable=False)
    usuario_id = db.Column(Integer, ForeignKey('usuarios.id', ondelete='CASCADE') ,nullable=False)
    quantidade = db.Column(Numeric(10,3),nullable=False,default=1)
    status = db.Column(Enum('pendente','comprado', name='status_enum'),default='pendente')
    categoria_id = db.Column(Integer, ForeignKey('categorias.id', ondelete='SET NULL') ,nullable=True)
    criado_em = db.Column(DateTime(),default=db.func.now(),onupdate=db.func.now())
    disponivel_em_casa = db.Column(Numeric(10,3),nullable=True,default=0)
    lista = db.relationship('Listas', backref=db.backref('itens', passive_deletes=True))
    categoria = db.relationship('Categorias', backref=db.backref('itens', passive_deletes=True))
    usuario = db.relationship('Usuarios', backref=db.backref('itens', passive_deletes=True))

    def __repr__(self):
        return f'<Item: {self.nome}>'


# Formulários de Login
from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length,EqualTo

class FormLogin(FlaskForm):
    
    email = EmailField('email',validators=[DataRequired(),Email(),Length(min=1,max=255)])
    senha = PasswordField('senha',validators=[DataRequired(),Length(min=1,max=255)])
    login_submit = SubmitField('Login')

class FormCadastro(FlaskForm):

    nome = StringField('nome',validators=[DataRequired(),Length(min=1,max=120)])
    email = EmailField('email',validators=[DataRequired(),Email(),Length(min=1,max=255)])
    senha = PasswordField('senha',validators=[DataRequired(),Length(min=1,max=255)])
    confirmar_senha = PasswordField('Confirmar Senha', validators=[DataRequired(),EqualTo('senha', message='As senhas devem coincidir')])
    cadastro_submit = SubmitField('Cadastrar')