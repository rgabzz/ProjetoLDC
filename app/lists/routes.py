from flask import render_template,abort,url_for,redirect
from app.lists import list_bp
from flask_login import login_required,current_user
from app.lists.helpers import owner_required,get_estoque,get_lista,Listas

@list_bp.route('/estoque')
@login_required
def estoque():
    
    lista_estoque = get_estoque()
    
    return render_template('estoque.html',lista_estoque=lista_estoque)


@list_bp.route('/<int:lista_id>')
@login_required
@owner_required
def lista(lista_id):

    if Listas.query.filter_by(id=lista_id, usuario_id=current_user.id).first_or_404().titulo == 'Estoque':
        return redirect(url_for('list.estoque'))
    
    lista = get_lista(lista_id)
    
    return render_template('lista.html',lista=lista)