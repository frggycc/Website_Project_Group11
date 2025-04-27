| Test Case ID | Title | Test Procedure | Expected Results | Status |
| ------------ | ------ | --------| ------------ | ------- |
| TC_001 | Home Page Route (/) | Click on the “Home” tab to trigger “Get / HTTP/1.1”. Click on the “Athletica Sportswear” to trigger “Get /HTTP/1.1”. | 200 OK, renders “home.html” and static images. | Pass |
| TC_002 | Women’s Clothing Route (/) | Hover over the “Women” tab and click on the “Clothing” tab to trigger “GET /women/clothing HTTP/1.1”. | 200 OK, renders “women_clothing.html” and static images. | Pass |
| TC_003 | Women’s Shoes Route (/) | Hover over the “Women” tab and click on the “Shoes” tab to trigger “GET /women/shoes HTTP/1.1”. | 200 OK, renders “women_shoes.html” and static images. | Pass |
| TC_004 | Women’s Accessory Route (/) | Hover over the “Women” tab and click on the “Accessory” tab to trigger “GET /women/accessory HTTP/1.1”. | 200 OK, renders “women_accessory.html” and static images. | Pass |
| TC_005 | Men’s Clothing Route (/) | Hover over the “Men” tab and click on the “Clothing” tab to trigger “GET /men/clothing HTTP/1.1”. | 200 OK, renders “men_clothing.html” and static images. | Pass |
| TC_006 | Men’s Shoes Route (/) | Hover over the “Men” tab and click on the “Shoes” tab to trigger “GET /men/shoes HTTP/1.1”. | 200 OK, renders “men_shoes.html” and static images. | Pass |
| TC_007 | Men’s Accessory Route (/) | Hover over the “Men” tab and click on the “Accessory” tab to trigger “GET /men/accessory HTTP/1.1”. | 200 OK, renders “men_accessory.html” and static images. | Pass |
| TC_008 | Search Items by Name | Input “Relay Sneakers” into search bar | 200 OK, results containing “Relay Sneakers,” static image render, option to add to cart appears. | Pass|
| TC_009 | Search Items by Color | Input “Red” into search bar | 200 OK, results containing “red” in their description, static images render, option to add to cart appears. | Pass|
| TC_010 | Search Items by Category | Input “Women” into search bar | 200 OK, results for Women clothing, shoes, accessories, static images render, option to put items into cart appears. | Pass |
| TC_011 | Search Items by Subcategory | Input “Shoes” into search bar | 200 OK, results for shoes under Men and Women category, static images render, option to put items into cart appears. | Pass |
| TC_012 | Search Items (No Results) | Input “adfadsfasd” into search bar | 200 OK, “No results found” message. | Pass |
| TC_013 | View Cart Page | Click shopping cart static image to GET /shopping-cart | 200 OK, renders “shopping_cart.html. All cart item’s static images render and the total price is displayed. | Pass |
| TC_014 | Add New Item to Shopping Cart | Search “Relay Sneakers” using the search bar. Click on the shopping cart button under “Relay Sneakers” to “/add_to_cart” | Item added to “session['shopping_cart']” with quantity = 1; redirect back to previous page or home. | Pass |
| TC_015 | Add Same Item to Shopping Cart | Search “Relay Sneakers” using the search bar. Click on the shopping cart button under “Relay Sneakers” to “/add_to_cart” twice. | Quantity of “Relay Sneakers” in session['shopping_cart'] increases by 1 | Pass |
| TC_016 | Session Persistence Shopping Cart | Add an item to the shopping cart. Navigate to the homepage. Click on the shopping cart image to return to /shopping-cart. | All items and their quantities are stored and remain correctly in session. | Pass |
| TC_017 | Load Admin Login Page | Navigate to /admin/login by entering URL into browser. | Admin login form (login.html) loads successfully with username and password fields. | Pass |
| TC_018 | Successful Admin Login | Enter correct credentials (username: admin, password: Group11) and submit the login form. | Redirect to Admin Dashboard (/admin). | Pass |
| TC_019 | Failed Admin Login (Wrong Password) | Enter correct username but incorrect password and submit the login form. | Stay on login page and display "Invalid credentials" message. | Pass |
| TC_020 | Failed Admin Login (Wrong Username) | Enter incorrect username and correct password and submit the login form. | Stay on login page and display "Invalid credentials" message. | Pass |
| TC_021 | Unauthorized Access to Admin Dashboard | Access /admin page directly without logging in. | Redirect automatically to /admin/login page. | Pass |
| TC_022 | View Admin Dashboard after Login | Log in as admin and navigate to /admin page. | Admin Dashboard loads showing all current items from database. | Pass |
| TC_023 | Add New Item in Admin Dashboard | Fill out "Add Item" form with valid item details and submit. | New item appears in the Admin Dashboard items list. | Pass |
| TC_024 | Edit Existing Item in Admin Dashboard | Edit an existing item’s name, price, or other details and submit the form. | Updated item details are saved to the database and displayed correctly. | Pass |
| TC_025 | Delete Item from Admin Dashboard | Delete an existing item by submitting the delete form for that item. | Selected item is removed from the Admin Dashboard list. | Pass |
| TC_026 | Admin Logout | Click on the Logout button on the Admin Dashboard. | Admin session ends and user is redirected to homepage (/). | Pass |

