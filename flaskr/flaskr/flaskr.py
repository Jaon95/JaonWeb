import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
render_template, flash
import click

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS',silent=True)

def connect_db():
    """connect to the specific database"""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """open a new database connection if there is none yet for  the current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """close the database again at the end of request.."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """initializes the database"""
    init_db()
    print('initializes the database ')
    
@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title, text from enries order by id desc')
    entries = cur.fetchall()
    return render_template('show_entries.html',entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries(title, text) values (?,?)',[request.form['title'], request.form['text']])
    db.commit()
    flash('new entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('you were logged in')
            return redirect(url_for(show_entries))
        return render_template('login.html',error=error)

@app.route('/logout')
def logout():
    session.pop('logged',None)
    flash('you were logged out')
    return redirect(url_for('show_entries'))