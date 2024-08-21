import sqlite3
import os

db_abs_path = os.path.dirname(os.path.realpath(__file__)) + '/kaggleworld.db'
conn = sqlite3.connect(db_abs_path)
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS datasets")
c.execute("DROP TABLE IF EXISTS categories")
c.execute("DROP TABLE IF EXISTS tags")
c.execute("DROP TABLE IF EXISTS comments")

c.execute("""CREATE TABLE categories(
                    id              INTEGER PRIMARY KEY AUTOINCREMENT,
                    name            TEXT
)""")

c.execute("""CREATE TABLE tags(
                    id              INTEGER PRIMARY KEY AUTOINCREMENT,
                    name            TEXT,
                    category_id     INTEGER,
                    FOREIGN KEY(category_id) REFERENCES categories(id)
)""")

c.execute("""CREATE TABLE datasets(
                    id              INTEGER PRIMARY KEY AUTOINCREMENT,
                    title           TEXT,
                    url             TEXT,
                    description     TEXT,
                    category_id     INTEGER,
                    tag_id          INTEGER,
                    FOREIGN KEY(category_id) REFERENCES categories(id),
                    FOREIGN KEY(tag_id) REFERENCES tags(id)
)""")

c.execute("""CREATE TABLE comments(
                    id              INTEGER PRIMARY KEY AUTOINCREMENT,
                    content         TEXT,
                    dataset_id      INTEGER,
                    FOREIGN KEY(dataset_id) REFERENCES items(id)
)""")

categories = [
    ("Computer Science",),
    ("Education",),
    ("Computer Vision",),
    ("NLP",),
    ("Data Visualization",),
    ("Pre-Trained Model",),
    ("Classification",)
]
c.executemany("INSERT INTO categories (name) VALUES (?)", categories)

tags = [
    ("Software", 1),
    ("Programming", 1),
    ("Jobs and Career", 2),
    ("Income", 2),
    ("Finance", 2),
    ("Investing", 3),
    ("Multiclass Classification", 3)
]
c.executemany("INSERT INTO tags (name, category_id) VALUES (?,?)", tags)

datasets = [
    ("Airbnb", "https://www.kaggle.com/datasets/paramvir705/airbnb-data", "property info", 2, 3),
    ("Walmart", "https://www.kaggle.com/datasets/mikhail1681/walmart-sales", "retail sales", 1, 1),
    ("Amazon", "https://www.kaggle.com/datasets/aaronfriasr/amazon-products-dataset", "sales data", 2, 5),
    ("Coffee", "https://www.kaggle.com/datasets/ihelon/coffee-sales", "vending sales data", 1, 2)
]
c.executemany("INSERT INTO datasets (title, url, description, category_id, tag_id) VALUES (?,?,?,?,?)", datasets)

comments = [
    ("This item is great!", 1),
    ("Whats up?", 2),
    ("Spam spam", 3)
]
c.executemany("INSERT INTO comments (content, dataset_id) VALUES (?,?)", comments)

conn.commit()
conn.close()

print("Database is created and initialized.")
print("You can see the tables with the show_tables.py script.")
