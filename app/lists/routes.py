from flask import render_template,abort,url_for,redirect
from app.lists import list_bp
from flask_login import login_required,current_user
from app.models import FormCriarItem
from app.lists.helpers import owner_required,get_estoque,get_lista,Listas,Categorias,criaritem

@list_bp.route('/estoque',methods=['GET','POST'])
@login_required
def estoque():

    lista_obj = Listas.query.filter_by(titulo='Estoque', usuario_id=current_user.id).first_or_404()
    
    lista_estoque = get_estoque()

    categorias = Categorias.query.all()

    form = FormCriarItem()
    form.categoria_id.choices = [(0, "Sem categoria")] + [
        (c.id, c.nome) for c in categorias
    ]

    if form.validate_on_submit():
        return criaritem(form,lista=lista_obj)
    
    
    return render_template('estoque.html',lista_estoque=lista_estoque,categorias=categorias,form=form,lista_obj=lista_obj)


@list_bp.route('/<int:lista_id>', methods=['GET', 'POST'])
@login_required
@owner_required
def lista(lista_id):

    lista_obj = Listas.query.filter_by(id=lista_id, usuario_id=current_user.id).first_or_404()

    if lista_obj.titulo == 'Estoque':
        return redirect(url_for('list.estoque'))
    
    lista = get_lista(lista_id)
    categorias = Categorias.query.all()

    form = FormCriarItem()
    form.categoria_id.choices = [(0, "Sem categoria")] + [
        (c.id, c.nome) for c in categorias
    ]

    if form.validate_on_submit():
        return criaritem(form,lista=lista_obj)
    
    return render_template('lista.html',lista=lista,categorias=categorias,form=form,lista_obj=lista_obj)
