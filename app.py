from flask import Flask, render_template, url_for, request, session, redirect
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "group_11"

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
                ("000005", "Fit Men T-Shirt", "Men", "Clothing", 19.99, "Fit_men_T-shirt.webp", "Cherry Red"),
                ("000006", "Divine Athletic Shirt", "Men", "Clothing", 19.99, "S-Divine Athletic T-Shirt.webp", "Black, Grey"),
                ("000007", "Sweatpants", "Men", "Clothing", 55.99, "Men_Grey_Sweats.webp", "Grey"),
                ("000008", "String Joggers", "Men", "Clothing", 53.99, "Men_Black_Joggers.jpeg", "Black"),
                ("000009", "Athletic Running Shoes", "Men", "Shoes", 79.99, "Athletic_Running_Shoes_Air.jpeg", "Black"),
                ("000010", "Golf Shoes High", "Men", "Shoes", 190.99, "Golf_Shoes_High_Men.webp", "Black, White, Gold"),
                ("000011", "Athletic Zipper Jacket", "Women", "Clothing", 39.99, "green_jacket_women.webp", "Green"),
                ("000012", "Long Sleeve", "Women", "Clothing", 19.99, "long_sleeve_women.jpg", "Blue"),
                ("000013", "Leggings", "Women", "Clothing", 39.99, "leggings_women.webp", "Black"),
                ("000014", "Drawstring Pants", "Women", "Clothing", 49.99, "drawstring_pants_women.jpg", "Grey"),
                ("000015", "Relay Sneakers", "Women", "Shoes", 89.99, "white_shoes_women.webp", "White, Black"),
                ("000016", "Running Shoes", "Women", "Shoes", 149.99, "running_shoes_women.jpg", "Purple, White")
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

@app.route('/women/shoes')
def women_shoes():
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM items WHERE category = 'Women' AND subcategory = 'Shoes'")
        items = cur.fetchall()
    return render_template("women_shoes.html", items=items)

@app.route('/men/clothing')
def men_clothing():
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM items WHERE category = 'Men' AND subcategory = 'Clothing'")
        items = cur.fetchall()
    return render_template("men_clothing.html", items=items)

@app.route('/men/shoes')
def men_shoes():
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM items WHERE category = 'Men' AND subcategory = 'Shoes'")
        items = cur.fetchall()
    return render_template("men_shoes.html", items=items)

# Creating a list for user ession that holds item id and quantity
@app.route('/add_to_cart', methods=["POST"])
def add_to_cart():
    item_id = request.form['item_id']

    # Create cart or update current
    if 'shopping_cart' not in session:
        session['shopping_cart'] = []
    
    # Increment item in cart if exists; Otherwise, add it to the cart
    for item in session['shopping_cart']:
        if item['id'] == item_id:
            item['quantity'] += 1
            break
    else:
        session['shopping_cart'].append({'id': item_id, 'quantity':1})

    session.modified = True

    return redirect(request.referrer or url_for('home'))

@app.route('/shopping-cart')
def shopping_cart():
    cart_items = []
    total_price = 0.0
    if 'shopping_cart' in session and session['shopping_cart']:
        with sqlite3.connect(DB_PATH) as con:
            cur = con.cursor()
            for cart_item in session['shopping_cart']:
                cur.execute("SELECT * FROM items WHERE id = ?", (cart_item['id'],))
                item = cur.fetchone()
                if item:
                    cart_items.append({
                        'id': item[0],
                        'name': item[1],
                        'category': item[2],
                        'subcategory': item[3],
                        'price': item[4],
                        'image': item[5],
                        'color': item[6],
                        'quantity': cart_item['quantity']
                    })
                    total_price += item[4] * cart_item['quantity']

    return render_template("shopping_cart.html", cart_items=cart_items, total_price=total_price)

@app.route('/search-Bar', methods=["GET", "POST"])
def search_bar():
    search_query = request.args.get("search", "").lower()
    print("Search Query:", search_query)

    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()

        if search_query:
            cur.execute("""
                SELECT * FROM items 
                WHERE LOWER(name) LIKE ?
                OR LOWER(category) LIKE ?
                OR LOWER(subcategory) LIKE ?
                OR LOWER(color) LIKE ?
            """, ['%' + search_query + '%'] * 4)
        else:
            cur.execute("SELECT * FROM items")

        items = cur.fetchall()
    print("Number of items found:", len(items))  # <-- Debug print
    for item in items:
        print(item)  # <-- Optional: print each item matched
    return render_template("base.html", items=items)

if __name__ == "__main__":
    if not os.path.exists(DB_PATH):
        init_db()

    app.run(debug=True)

