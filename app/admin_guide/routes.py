from app.admin_guide import adm_bp
from flask import render_template,flash,redirect,url_for
from app.models import Usuarios,db,Categorias
from app.admin_guide.forms import FormCriarCategoria
from app.admin_guide.helpers import adm_required


@adm_bp.route('/usuarios')
@adm_required
def usuarios():

    lista_usuarios = Usuarios.query.order_by(Usuarios.id)

    return render_template('admin_guide/usuarios.html',lista_usuarios=lista_usuarios)

@adm_bp.route('/usuarios/deletar/<int:id>')
@adm_required
def deletar_usuario(id):

    Usuarios.query.filter_by(id=id).delete()
    db.session.commit()

    return redirect(url_for('painel.usuarios'))

@adm_bp.route('/categorias',methods=['POST','GET'])
@adm_required
def categorias():
    lista_categorias = Categorias.query.order_by(Categorias.id)

    form = FormCriarCategoria()

    if form.validate_on_submit():
        nome = form.nome.data

        if Categorias.query.filter_by(nome=nome).first():
            flash('Essa categoria já existe')
        
        else:

            nova_categoria  = Categorias(nome=nome)
            db.session.add(nova_categoria)
            db.session.commit()

        form.nome.data = ''

    return render_template('admin_guide/categorias.html',lista_categorias=lista_categorias,form=form)

@adm_bp.route('/categorias/deletar/<int:id>')
@adm_required
def deletar_categoria(id):

    Categorias.query.filter_by(id=id).delete()
    db.session.commit()

    return redirect(url_for('painel.categorias'))