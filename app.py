from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home(): 
    return render_template('index.html')

@app.route('/about')
def about():
    # return "<p>Hello, World!</p>"
    name = "Joshua Farara"
    age = 28
    occupation = "Visiting Instructor of Computer Science at Georgia Southern University"
    undergrad = "BS in Economics"
    masters =  "MS in Computer Science"
    return render_template('about.html', name=name, age=age, occupation=occupation, undergrad=undergrad, masters=masters)

@app.route('/notebook-dashboard')
def notebooks():
    notebooks_folder = './notebooks'
    notebooks = os.listdir(notebooks_folder)
    return render_template('notebook-dashboard.html', notebooks=notebooks)