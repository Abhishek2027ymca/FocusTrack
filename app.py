from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime, nullable=True)
    category = db.Column(db.String(100), nullable=True)
    completed = db.Column(db.Boolean, default=False)
    priority = db.Column(db.String(20), default='Medium')

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        due_date = request.form.get('due_date')
        category = request.form.get('category')
        priority = request.form.get('priority', 'Medium')
        todo = Todo(
            title=title,
            desc=desc,
            due_date=datetime.strptime(due_date, '%Y-%m-%d') if due_date else None,
            category=category,
            priority=priority
        )
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo, now=datetime.now)

@app.route('/show')
def products():
    allTodo = Todo.query.all()
    print(allTodo)
    return 'this is products page'

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    if request.method=='POST':
        todo.title = request.form['title']
        todo.desc = request.form['desc']
        due_date = request.form.get('due_date')
        category = request.form.get('category')
        priority = request.form.get('priority', 'Medium')
        todo.due_date = datetime.strptime(due_date, '%Y-%m-%d') if due_date else None
        todo.category = category
        todo.priority = priority
        todo.completed = 'completed' in request.form
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    return render_template('update.html', todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
