# Import Flask and render_template from the flask module
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

# Create an instance of the Flask class (the web app)
app = Flask(__name__)

## initialiinf alschemy 
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
## it is usde for signal emmiting 
db = SQLAlchemy(app)


## defining the schema of database 
class Todo(db.Model):
        sno = db.Column(db.Integer, primary_key = True)
        title  = db.Column(db.String(200), nullable = False)
        desc = db.Column(db.String(500), nullable = False)
        date_created = db.Column(db.DateTime, default = datetime.utcnow)

####### creatingan repr method 
        def __repr__(self) -> str:
            return f"{self.sno} - {self.title}"
@app.route('/')
def home():
    # Create an instance of the Todo model (a single todo item)
    # This will have title = "First Todo" and description = "Start investing in stock market"
    todo = Todo(title="First Todo", desc="Start investing in stock market")
    
    # Add the new todo instance to the current database session
    db.session.add(todo)
    
    # Commit the session so the change is actually written to the database
    db.session.commit()
    
    # Successfully committed the changes, now render the index.html template
    return render_template('index.html')

    # This will render 'index.html' from the 'templates/' folder
    #return render_template("index.html")

# Define another route '/pro' for testing or another page
@app.route("/pro")
def pro():
    # This route simply returns a plain text response
    return "prod page is this"

# Check if this file is being run directly (not imported)
if __name__ == "__main__":
    # Run the app in debug mode (auto reloads on changes + shows errors)
    app.run(debug=True)

## now creating a data  base 
## we have to  tell that what we need tos  store to flask and it will handle it 

## by installing flask sequel alchmi 
## it is an orm mapper 
