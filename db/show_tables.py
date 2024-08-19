import sqlite3
import os

db_abs_path = os.path.dirname(os.path.realpath(__file__)) + '/kaggleworld.db'

print("Options: (datasets, comments, categories, tags, all)")
table = input("Show table: ")

conn = sqlite3.connect(db_abs_path)
c = conn.cursor()

def show_datasets():
    try:
        datasets = c.execute("""SELECT
                                d.id, d.title, d.description, d.price, d.image, c.name, c.id, t.name, t.id
                             FROM
                                datasets AS d
                             INNER JOIN categories     AS c ON d.category_id     = c.id
                             INNER JOIN tags           AS t ON d.tag_id          = t.id
        """)

        print("DATASETS")
        print("#############")
        for row in datasets:
            print("ID:             ", row[0]),
            print("Title:          ", row[1]),
            print("Url:            ", row[2]),
            print("Description:    ", row[3]),
            print("Category:       ", row[5], "(", row[6], ")"),
            print("Tag:            ", row[7], "(", row[8], ")"),
            print("\n")
    except:
        print("Something went wrong, please run db_init.py to initialize the database.")
        conn.close()

def show_comments():
    try:
        comments = c.execute("""SELECT
                                    c.id, c.content, d.title, d.id
                                 FROM
                                    comments AS c
                                 INNER JOIN datasets AS d ON c.dataset_id = d.id
        """)

        print("COMMENTS")
        print("#############")
        for row in comments:
            print("ID:             ", row[0]),
            print("Content:        ", row[1]),
            print("Dataset:        ", row[2], "(", row[3], ")")
            print("\n")
    except:
        print("Something went wrong, please run db_init.py to initialize the database.")
        conn.close()

def show_categories():
    try:
        categories = c.execute("SELECT * FROM categories")

        print("CATEGORIES")
        print("#############")
        for row in categories:
            print("ID:             ", row[0]),
            print("Name:           ", row[1])
            print("\n")
    except:
        print("Something went wrong, please run db_init.py to initialize the database.")
        conn.close()

def show_tags():
    try:
        tags = c.execute("SELECT t.id, t.name, c.name, c.id FROM tags AS t INNER JOIN categories AS c ON t.category_id = c.id")
        print("TAGS")
        print("#############")
        for row in tags:
            print("ID:             ", row[0]),
            print("Name:           ", row[1]),
            print("Category:       ", row[2], "(", row[3], ")")
            print("\n")
    except:
        print("Something went wrong, please run db_init.py to initialize the database.")
        conn.close()


if table == "datasets":
    show_datasets()
elif table == "comments":
    show_comments()
elif table == "categories":
    show_categories()
elif table == "tags":
    show_tags()
elif table == "all":
    show_datasets()
    show_comments()
    show_categories()
    show_tags()
else:
    print("This option does not exist.")

conn.close()
