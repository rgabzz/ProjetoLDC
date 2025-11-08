from functools import wraps
from flask import redirect, url_for,abort
from flask_login import current_user

def adm_required(f):
    @wraps(f)
    def adm(*args, **kwargs):
        if current_user.cargo != 'admin':
            abort(403)
        return f(*args, **kwargs)
    return adm