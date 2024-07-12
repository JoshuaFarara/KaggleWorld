from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # return "<p>Hello, World!</p>"
    name = "Joshua Farara"
    age = 28
    occupation = "Visiting Instructor of Computer Science at Georgia Southern University"
    undergrad = "BS in Economics"
    masters =  "MS in Computer Science"
    
    return render_template('index.html', name=name, age=age, occupation=occupation, undergrad=undergrad, masters=masters)

@app.route('/data-analysis')
def data_analysis():
    pass