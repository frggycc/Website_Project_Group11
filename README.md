
# Group 11 – E-Commerce Web App

CPSC 362 Project Documentation  
Team Members:  
- Ellie Winter  
- Jake Miso  
- Charlie Jimenez  
- Yordy Sanchez  
- Anchal Brar  

---

## Overview

### Product Vision

Our team developed a fashion e-commerce website inspired by modern retail platforms like NIKE, with an emphasis on athleticism, comfort, and modern style. The goal is to provide a clean, intuitive, and responsive shopping experience.

Customers can browse, search, and purchase items by adding them to their cart. Unlike competitors, we aim to deliver innovative clothing that reflects the lifestyle and needs of active individuals. This is performance-driven fashion that supports athletic excellence and reflects everyday confidence.

---

## Running the Application

### Technologies Used

- Python (Flask)
- SQLite

### Setup Instructions

Ensure Python and Flask are installed on your system:

```
pip install flask
```

Then, run the application:

```
python app.py
```

Once the app is running, visit the site in your browser:

```
http://127.0.0.1:5000/
```

---

## Application Flow

### Home Page (/)

- Displays featured items fetched from the database.

### Category Navigation

- URLs like /women/clothing/ or /men/shoes/ are used to fetch and display products based on their section and subsection.

### Add to Cart (/add_to_cart)

- Triggered by a POST request when a user adds an item.
- Saves the item ID and quantity in session['shopping_cart'].

### Search (/search-bar)

- Accepts a keyword and performs a query across product name, category, and subcategory.

---

### Admin Features

- Admin login -  /admin/login  
  - Simple login form for the admin.

- Admin Panel - /admin  
  - Allows the admin to:
    - Add new products
    - Edit existing products
    - Delete products

- Logout: /admin/logout  
  Logs out the admin by removing their session variable.

---

## Requirements

### Functional Requirements

| ID | Identity | Description |
| ----------- | ----------- | ------|
| FR_0 | Homepage | Users will be able to access a homepage when opening a link to the website. It will be the access point to mulitple features. |
| FR_1 | Searchbar | Users can search for products using keywords. Search returns results from product name, section, and subsection. |
| FR_2 | Shopping Cart | Users can add items to their cart, modify quantities, and proceed to checkout. |
| FR_3 | User Account Management | Users are able to login and create an account |
| FR_4 | Product Catalog Management | Products can be added, updated, or deleted by an admin. Each product includes a price, description, and image. |
| FR_5 | Checkout and Orders | Users can place orders. Orders are stored with user details. |
| FR_6 | Men | Users will be able to search for a variety of men's products. |
| FR_7 | Women | Users will be able to search for a variety of women's products. |

---

### Non-Functional Requirements

| ID | Identity | Description |
| ----------- | ----------- | ------|
| NFR_0 | Loading Time & Performance | The pages on the website should be able to load in 2 seconds when the total number of simultaneous users is less than 6 thousand. |
| NFR_1 | Scalability | The amount of items can increase in the database. Can support an increasing numbers of Users |
| NFR_2 | Availability | Should always be available to access and maintain a 90% uptime, ensuring it is always accessible to users. |
| NFR_3 | Security | Protect sensitive data, and be able to protect the database. Should keep user information safe |
| NFR_4 | Region Accessibility | The website should be made available in US, UN, and Canadian regions to ensure a wide geographic accessibility. |
