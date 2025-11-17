from flask import Blueprint,render_template
from flask_login import login_required,current_user
from app.models import Listas
from app.lists.helpers import get_estoque

main_bp = Blueprint('main',__name__)

@main_bp.route('/')
@login_required
def index():

    lista_usuario = (
    Listas.query
    .filter(
        Listas.usuario_id == current_user.id,
        Listas.titulo != "Estoque"
    )
    .order_by(Listas.id.asc())
    .first()
)
    
    lista_estoque = (
    Listas.query
    .filter(
        Listas.usuario_id == current_user.id,
        Listas.titulo == "Estoque"
    )
    .first()
)

    return render_template('index.html', username=getattr(current_user, 'nome', 'Visitante'),lista_usuario=lista_usuario,lista_estoque=lista_estoque)