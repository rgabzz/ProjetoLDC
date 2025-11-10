from flask import render_template,abort,url_for,redirect,request, flash
from app.lists import list_bp
from flask_login import login_required,current_user
from app.lists.helpers import owner_required,get_estoque,get_lista,Listas 
from app.models import Itens, Listas, RelacaoItensListas, Categorias, db

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

@list_bp.route('/<int:lista_id>/novo_item', methods=['GET', 'POST'])
@login_required
@owner_required
def criar_item(lista_id):
    lista = Listas.query.get_or_404(lista_id)

    # Busca todas as categorias do usuário para preencher o select
    categorias = Categorias.query.all()

    if request.method == 'POST':
        nome = request.form.get('nome')
        quantidade = request.form.get('quantidade')
        categoria_id = request.form.get('categoria_id')

        print("VALOR ENVIADO PELO FORMULÁRIO:", quantidade)

        # --- Validações básicas ---
        if not nome or not quantidade:
            flash('Preencha todos os campos obrigatórios.', 'warning')
            return render_template('criar_item.html', lista=lista, categorias=categorias)

        try:
            quantidade = float(quantidade)
        except (ValueError, TypeError):
            quantidade = 1  # valor padrão se vier vazio

        try:
            quantidade = float(quantidade)
        except ValueError:
            flash('A quantidade precisa ser um número.', 'warning')
            return render_template('criar_item.html', lista=lista, categorias=categorias)

        if categoria_id == '0' or not categoria_id:
            categoria_id = None

        # --- Criação do item ---
        novo_item = Itens(
            nome=nome,
            quantidade=quantidade,
            status='pendente',
            usuario_id=current_user.id,
            categoria_id=categoria_id
        )

        db.session.add(novo_item)
        db.session.flush()  # garante que novo_item.id exista

        relacao = RelacaoItensListas(
            lista_id=lista.id,
            item_id=novo_item.id
        )
        db.session.add(relacao)
        db.session.commit()

        print("ITEM SALVO:", novo_item.quantidade)

        flash('Item criado com sucesso!', 'success')
        return redirect(url_for('list.lista', lista_id=lista.id))

    # Se GET → exibe o formulário
    return render_template('criar_item.html', lista=lista, categorias=categorias)
