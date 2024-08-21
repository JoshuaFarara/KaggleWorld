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
    notebooks_folder = './notebooks'
    notebooks = os.listdir(notebooks_folder)
    return render_template('notebook-dashboard.html', notebooks=notebooks)

'''Base notebook dashboard navigation'''
@app.route('/notebook-dashboard/datasets')
def datasets():
    conn = get_db()
    c = conn.cursor()
    datasets_from_db = c.execute("""SELECT
                            d.id, d.title, d.url, d.description, c.name, c.id, t.name, t.id
                            FROM
                               datasets AS d
                            INNER JOIN categories     AS c ON d.category_id     = c.id
                            INNER JOIN tags           AS t ON d.tag_id          = t.id
                            ORDER BY d.id DESC
        """)
    datasets = []
    for row in datasets_from_db:
        dataset = {
            "id": row[0],
            "title": row[1],
            "url": row[2],
            "description": row[3],
            "category": row[4],
            "tag": row[5],
        }
        datasets.append(dataset)

    notebooks_folder = './notebooks'
    notebooks = os.listdir(notebooks_folder)

    return render_template('datasets.html', datasets=datasets, notebooks=notebooks)

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
                        request.form.get("title"),
                        request.form.get("url"),
                        request.form.get("description"),
                        1,
                        1
                    )
        )
        conn.commit()
        # Redirect to some page
        return redirect(url_for("datasets"))
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