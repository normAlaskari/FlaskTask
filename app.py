# imports
from flask import Flask, render_template, redirect, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# App
app = Flask(__name__)
Scss(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dataBase.db'
db = SQLAlchemy(app)

class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    isCompleted = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Task {self.id}>'

@app.route("/", methods=["POST", "GET" , "DELETE"])
def index():
    # Add Task
    if request.method == "POST":
        current_task = request.form['content']
        new_task = MyTask(content=current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"Error: {e}"
    # See all current tasks
    else:
        tasks = MyTask.query.order_by(MyTask.created).all()
        return render_template("index.html", tasks=tasks)
    
@app.route("/delete/<int:id>")
def delete(id:int):
    task_to_delete = MyTask.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"Error: {e}"
    
@app.route("/update/<int:id>", methods=["POST", "GET"])
def update(id:int):
    task = MyTask.query.get_or_404(id)
    if request.method == "POST":
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"Error: {e}"
    else:
        return render_template("edit.html", task=task)
    
@app.route("/complete/<int:id>", methods=["POST"])
def complete(id:int):
    task = MyTask.query.get_or_404(id)
    if request.method == "POST":
        task.isCompleted = not task.isCompleted
    try:
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
