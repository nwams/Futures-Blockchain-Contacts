#imports
import os
from flask import Flask, render_template, request, session, g, redirect, url_for, abort, flash
#from sqlite3 import dbapi2 as sqlite3
#from contextlib import closing
#from flask.ext.sqlalchemy import SQLAlchemy

#set up our app
app = Flask(__name__)
#app.config.from_envvar('APP_SETTINGS', silent=True)

# configuration
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY = 'secretkey',
    USERNAME='username',
    PASSWORD='password'
))
#app.config.from_envvar('FLASKR_SETTINGS', silent=True)


# configuration of database for our blog
#app.config.update(dict(
    #DATABASE = os.path.join(app.root_path, 'app.db'),
    #DEBUG = True,
    #SECRET_KEY = 'password',
    #USERNAME = 'admin',
    #PASSWORD = 'default'
#))


#def connect_db():                 #connects to the database we specified above
    #rv = sqlite3.connect(app.config['DATABASE'])
    #rv.row_factory = sqlite3.Row
    #return rv

#def init_db():                   #initialize database
    #db = get_db()
    #with app.open_resource('schema.sql', mode='r') as f:
        #db.cursor().executescript(f.read())
    #db.commit()

#@app.cli.command('initdb')           #creates database tables
#def initdb_command():
    #init_db()
    #print('Initialized the database.')

#def get_db():           #opens a database connection if there is none yet for the current application context
    #if not hasattr(g, 'sqlite_db'):
        #g.sqlite_db = connect_db()
    #return g.sqlite_db

#configure our SQLAlchemy DB
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#db = SQLAlchemy(app)

#set up a class for user database
#class User(db.Model):
    #id = db.Column(db.Integer, primary_key=True)        #defines a column called id
    #username = db.Column(db.String(80), unique=True)    #defines a column called username
    #email = db.Column(db.String(120), unique=True)      #defines a column called email

    #def __init__(self, username, email):
        #self.username = username
        #self.email = email

    #def __repr__(self):
        #return '<User %r>' % self.username

#@app.teardown_appcontext               #closes database at end of request
#def close_db(error):
    #if hasattr(g, 'sqlite_db'):
        #g.sqlite_db.close()

#@app.route('/blog')
#def show_entries():
    #db = get_db()
    #cur = db.execute('select title, text from entries order by id desc')
    #entries = cur.fetchall()
    #return render_template('show_entries.html', entries=entries)

#@app.route('/add', methods=['POST'])
#def add_entry():
    #if not session.get('logged_in'):
        #abort(401)
    #db = get_db()
    #db.execute('insert into entries (title, text) values (?, ?)',
               #[request.form['title'], request.form['text']])
    #db.commit()
    #flash('New entry was successfully posted')
    #return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('main'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('main'))

#when the user comes to the main page, send them to the index template
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/futureethereum')
def main_future():
    return render_template('futureethereum.html')

@app.route('/optionethereum')
def main_option():
    return render_template('optionethereum.html')

@app.route('/swapethereum')
def main_swap():
    return render_template('swapethereum.html')

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

#we will use this to add the info of a new user to the DB:
#new_user = User('admin', 'admin@example.com')
#db.session.add(new_user)
#db.session.commit()

if __name__ == '__main__':
    #app.debug = True
    #app.run(debug=True)
    #app.run(debug=True, port=5001)
    #app.run(host='0.0.0.0')   #turn this on later when you go to another server
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
