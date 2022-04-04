from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

import re

app = Flask(__name__)

# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


def task(request):

   view=request.args.get('view', '')

   if 'add' in view: 
      return addpage(request)

   if 'delete' in view: 
      return  deletepage(request)

   if 'update' in view: 
       return updatepage(request)

   if 'todo' in view: 
       return home()


def account(request):
   print("hai")
   view=request.args.get('view', '')
   if 'edit' in view: 
       return editpage(request)
   if 'do' in view: 
        return dopage(request)
   if 'erase' in view: 
        return erasepage(request)
   if 'user' in view: 
       return newhome()



# @app.route("/todo")
def home():
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template("base.html", todo_list=todo_list)

#route_regex = re.compile(r'^todo/add/')

# @app.route("/add")
def addpage(request):
    title=request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect("todo?view=todo")



# @app.route("/update/<int:todo_id>")
def updatepage(request):
    todo_id=request.args.get('todo_id', '')
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect("todo?view=todo")


# @app.route("/delete/<int:todo_id>")
def deletepage(request):
    todo_id=request.args.get('todo_id', '')
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("todo?view=todo")


#@app.route("/newhome")
def newhome():
    todo_list = Todo.query.all()
    return render_template("index.html", todo_list=todo_list)

#@app.route("/edit", methods=["POST"])
def editpage(request):
    #todo_id=request.args.get('todo_id', '')
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect("user?view=user")
    


#@app.route("/do/<int:todo_id>")
def dopage(request):
    todo_id=request.args.get('todo_id', '')
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    #return redirect(url_for("newhome"))
    return redirect("user?view=user")
    

#@app.route("/erase/<int:todo_id>")
def erasepage(request):
    print("***hai")
    todo_id=request.args.get('todo_id', '')
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    #return redirect(url_for("newhome"))
    return redirect("user?view=user")


@app.route("/todo", methods=["GET", "POST"])
def fun():
    return task(request)

@app.route("/user", methods=["GET", "POST"])
def fun1():
    return account(request)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)


