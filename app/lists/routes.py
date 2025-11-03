from flask import render_template
from app.lists import list_bp
from flask_login import login_required
from app.lists.helpers import get_estoque

@login_required
@list_bp.route('/estoque')
def estoque():
    
    lista_estoque = get_estoque()
    
    return render_template('estoque.html',lista_estoque=lista_estoque)