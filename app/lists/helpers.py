from app.models import Itens,Listas,Categorias,Usuarios,RelacaoItensListas,db
from flask_login import current_user
from flask import flash
from functools import wraps
from flask import abort,redirect,url_for

def owner_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        lista_id = kwargs.get('lista_id')

        lista = Listas.query.filter_by(id=lista_id, usuario_id=current_user.id).first()

        if not lista:
            abort(403)

        return f(*args, **kwargs)
    return decorated_function

def criaritem(form, lista):
    categoria_escolhida = form.categoria_id.data

    if categoria_escolhida == 0:
        categoria_escolhida = None

    novo_item = Itens(
        nome=form.nome.data,
        quantidade=form.quantidade.data,
        status='pendente',
        usuario_id=current_user.id,
        categoria_id=categoria_escolhida
    )

    db.session.add(novo_item)
    db.session.flush()

    relacao = RelacaoItensListas(
        lista_id=lista.id   ,
        item_id=novo_item.id
    )

    db.session.add(relacao)
    db.session.commit()

    #flash("Item criado com sucesso!", "success")
    return redirect(url_for('list.lista', lista_id=lista.id))



def get_estoque():

    lista = (db.session.query(
        Itens.nome.label('item_nome'),
        Itens.disponivel_em_casa,
        Itens.status,
        Categorias.nome.label('categoria_nome')
    )
    .join(Categorias, Itens.categoria_id == Categorias.id)
    .join(RelacaoItensListas, RelacaoItensListas.item_id == Itens.id)
    .join(Listas, Listas.id == RelacaoItensListas.lista_id)
    .filter(Itens.usuario_id == current_user.id)
    .filter(Listas.titulo == 'Estoque')
    .filter(Listas.usuario_id == current_user.id)
    .all()
    )

    return lista

def get_lista(lista_id):
    lista = (db.session.query(
        Itens.nome.label('item_nome'),
        Itens.quantidade,
        Itens.status,
        Itens.criado_em.label('criado'),
        Categorias.nome.label('categoria_nome')
    )
    .join(Categorias, Itens.categoria_id == Categorias.id)
    .join(RelacaoItensListas, RelacaoItensListas.item_id == Itens.id)
    .join(Listas, Listas.id == RelacaoItensListas.lista_id)
    .filter(Itens.usuario_id == current_user.id)
    .filter(Listas.id == lista_id)
    .filter(Listas.usuario_id == current_user.id)
    .all()
    )



    '''for row in lista:
        print(row.item_nome)'''

    return lista



