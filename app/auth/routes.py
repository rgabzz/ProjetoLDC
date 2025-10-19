from flask import render_template,redirect,url_for,flash
from flask_login import login_user,logout_user,login_required
from app import login_manager,db
from app.auth import auth_bp
from app.models import Usuarios,FormCadastro,FormLogin
from werkzeug.security import generate_password_hash,check_password_hash

@auth_bp.route('/login', methods=['GET','POST'])
def login():

    form = FormLogin()

    if form.validate_on_submit():
        usuario = Usuarios.query.filter_by(email=form.email.data).first()

        if usuario and check_password_hash(usuario.senha_hash,form.senha.data):
            login_user(usuario)

            return redirect(url_for('main.index'))


    return render_template('login.html',form=form)

@auth_bp.route('/cadastro', methods=['GET','POST'])
def cadastro():

    form = FormCadastro()

    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        senha_hash = generate_password_hash(form.senha.data)

        if Usuarios.query.filter_by(email=email).first():
            flash('Já existe alguém utilizando esse email')

        else:
            novo_usuario = Usuarios(nome=nome,email=email,senha_hash=senha_hash)
            db.session.add(novo_usuario)
            db.session.commit()

            return redirect(url_for('auth.login'))

    return render_template('cadastro.html',form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@login_manager.user_loader
def load_user(user_id):
    return Usuarios.query.get(int(user_id))