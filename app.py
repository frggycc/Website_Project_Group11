from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

''' DATABASE '''
# Set up database
DB_PATH = "database.db"

def init_db():
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()

        # Create item table
        cur.execute('''CREATE TABLE IF NOT EXISTS items
                    (id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    subcategory TEXT NOT NULL,
                    price REAL NOT NULL,
                    image TEXT,
                    color TEXT)''')
        
        # Enter sample data; Fill table with this data only if empty
        cur.execute("SELECT COUNT(*) FROM items")
        if cur.fetchone()[0] == 0:
            sample_items = [
                ("000001", "Checkered Overalls", "Women", "Clothing", 39.99, "checker_overalls.jpg", "Red, Black"),
                ("000002", "Vest Dress", "Women", "Clothing", 54.99, "vest_dress.jpg", "Brown"),
                ("000003", "Athletic Crew T-Shirt", "Men", "Clothing", 19.99, "athletic_crew_tshirt.jpg", "Navy"),
                ("000004", "Patriotic Loose Shirt", "Men", "Clothing", 21.99, "patriotic_loose_shirt.jpg", "Blue"),
                ("000005", "Fit Men T-Shirt", "CLothing", "Clothing", 19.99, "Fit_men_T-shirt.webp", "Cherry Red")
               
            ]
            cur.executemany("INSERT INTO items (id, name, category, subcategory, price, image, color) VALUES (?, ?, ?, ?, ?, ?, ?)", sample_items)
        
        con.commit()

''' ROUTES '''
''' 
This will determine the html page to display based on file linked to the name of the page. So if we have an 
html file for women.html, we will create a path to it --> "@app.route('/women')" where "/women" is our path.

If you wanted to append another path to the end of an existing path (a slug), then just change the path by 
appending the name of the html file to the main subdirectory. So if we have an html file for women-shoes.html, 
we will create a path --> "@app.route('/women/women-shoes')" where "/women/women-shoes" is our path

Additionally, this is where we can manipulate our table based on the page the user is currently in. 
'''

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/women/clothing')
def women_clothing():
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM items WHERE category = 'Women' AND subcategory = 'Clothing'")
        items = cur.fetchall()
    return render_template("women_clothing.html", items=items)

@app.route('/men/clothing')
def men_clothing():
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM items WHERE category = 'Men' AND subcategory = 'Clothing'")
        items = cur.fetchall()
    return render_template("men_clothing.html", items=items)

if __name__ == "__main__":
    if not os.path.exists(DB_PATH):
        init_db()

    app.run(debug=True)
