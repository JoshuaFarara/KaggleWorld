from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"
    name = "Joshua Farara"
    age = 28
    occupation = "Visiting Instructor of Computer Science at Georgia Southern University"
    undergrad = "BS in Economics"
    masters =  "MS Computer Science"
    
    return render_template('index.html', name=name, age=age, occupation=occupation, undergrad=undergrad, masters=masters)