from app.models import Itens,Listas,Categorias,Usuarios,RelacaoItensListas,db
from flask_login import current_user

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

    for row in lista:
        print(row.item_nome, row.disponivel_em_casa, row.status, row.categoria_nome)

    return lista


# Fzr decorator pra a lista que o usuário puder pegar ser dele list/1 se n for dele da proibiido de entrar!

