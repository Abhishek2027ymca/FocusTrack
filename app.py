# Import Flask and render_template from the flask module
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

# Create an instance of the Flask class (the web app)
app = Flask(__name__)

# Initialize SQLAlchemy 
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Defining the schema of database 
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

# Create the database if it doesn't exist
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']

        # Create a new Todo entry
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()

    # Always fetch all todos for rendering
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo) 

@app.route('/show')
def products():
    allTodo = Todo.query.all()
    print(allTodo)
    return render_template("index.html", allTodo=allTodo)

if __name__ == "__main__":
    app.run(debug=True)
