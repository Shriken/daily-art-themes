from flask import session, redirect, url_for
from code import interact

def repl(moreLocals):
    local = locals()
    local.update(moreLocals)
    interact(local=local)

def require_login(func):
    def new_func(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        else:
            return func(*args, **kwargs)
    new_func.__name__ = func.__name__

    return new_func
