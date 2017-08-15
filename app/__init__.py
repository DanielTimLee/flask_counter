from flask import Flask, render_template, request, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static')
app.config.from_object('config')

db = SQLAlchemy(app)

from app.models import *
db.create_all()


from app.models.todo import TodoModel

@app.route('/')
def index():
    a=request.cookies.get('counter')
    if a:
        a=int(a)

    if not a:
        a=1
    else:
        a=a+1

    resp = make_response(render_template('index.html',a=a))
    resp.set_cookie('counter',str(a))
    return resp

@app.route('/todo', methods=['GET','POST'])
def todo():

    if request.method == 'POST':
        print(request.form['todo'])
        
        new_todo = TodoModel(
            content=request.form['todo']
        )

        db.session.add(new_todo)
        db.session.commit()

    todos = TodoModel.query.all()

    return render_template('todo.html',todos=todos)
