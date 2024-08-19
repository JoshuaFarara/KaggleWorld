from flask import Flask, request, render_template, redirect, url_for, g
import sqlite3
import os
import subprocess
import threading


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

'''Base notebook dashboard navigation'''
@app.route('/notebook-dashboard')
def notebooks():
    # Start the Streamlit app if it's not already running
    # if 'STREAMLIT_SERVER' not in os.environ:
    #     os.environ['STREAMLIT_SERVER'] = '1'
    #     subprocess.Popen(["streamlit", "run", "streamlit_app.py"])

    notebooks_folder = './notebooks'
    notebooks = os.listdir(notebooks_folder)
    return render_template('notebook-dashboard.html', notebooks=notebooks)

@app.route('/new-notebook', methods=["GET", "POST"])
def new_notebook():
    conn = get_db()
    c = conn.cursor()

    if request.method == "POST":
        # Process the form data
        c.execute("""INSERT INTO datasets
                    (title, url, description, category_id, tag_id)
                    VALUES (?,?,?,?,?)""",
                    (
                        request.form.get("dataset_url"),
                        request.form.get("title"),
                        request.form.get("description"),
                        1,
                        1
                    )
        )
        conn.commit()
        # Redirect to some page
        return redirect(url_for("home"))
    return render_template('new-notebook.html')

'''Display data within the notebook dashboard'''
@app.route('/cofee_sales')
def cofee_sales():
    def run_streamlit():
        if 'STREAMLIT_SERVER' not in os.environ:
            os.environ['STREAMLIT_SERVER'] = '1'
            subprocess.Popen(["streamlit", "run", "coffee_sales_streamlit.py"], 
                 creationflags=subprocess.CREATE_NO_WINDOW, 
                 stdout=subprocess.PIPE, 
                 stderr=subprocess.PIPE)
        # subprocess.run(["streamlit", "run", "coffee_sales_streamlit.py"])

    thread = threading.Thread(target=run_streamlit)
    thread.start()
    return render_template('cofee_sales.html')

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("db/kaggleworld.db")
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run(debug=True)