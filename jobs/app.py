from flask import g, Flask
from flask import render_template
from flask import sqlite3

PATH = "db/jobs.sqlite"
app = Flask(__name__)

def open_connection():
    connection = getattr(g, '_connection', 'None')
    if connection is None:
        connection = g._connection = sqlite3.connect(PATH)
    connection.row_factory = sqlite3.Row
    return connection

def execute_sql(sql, values, commit, single):
    connection = open_connection()
    values = ()
    commit = False
    single = False
    cursor = connection.execute(sql, values)
    if commit is True:
        results = connection.commit()
    else:
        results = cursor.fetchone() if single else cursor.fetchall()
    cursor.close()
    return results

def close_connection(exception):
    connection = getattr(g, '_connection', 'None')
    if connection is not None:
        connection.close()
    @app.teardown_appcontext
    
    
    
            

@app.route('/')
@app.route('/jobs')
def jobs ():
    return render_template('index.html')

