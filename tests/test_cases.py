import unittest
import sqlite3
from flask import Flask
from app import app, DB_PATH

class WebTestCases(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
        self.app.config['SECRET_KEY'] = 'test_secret_key'
        
        # Connect to database
        self.con = sqlite3.connect(DB_PATH)
        self.cursor = self.con.cursor()

    def tearDown(self):
        self.con.close()

    def test_home_page(self):
        """ TC_001: Home page loads successfully """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_women_clothing_page(self):
        """ TC_002: Women's clothing page loads successfully """
        response = self.client.get('/women/clothing')
        self.assertEqual(response.status_code, 200)
    
    def test_women_shoes_page(self):
        """ TC_003: Women's shoes page loads successfully """
        response = self.client.get('/women/shoes')
        self.assertEqual(response.status_code, 200)

    def test_women_accessories_page(self):
        """ TC_004: Women's accessories page loads successfully """
        response = self.client.get('/women/accessories')
        self.assertEqual(response.status_code, 200)

    def test_men_clothing_page(self):
        """ TC_005: Men's clothing page loads successfully """
        response = self.client.get('/men/clothing')
        self.assertEqual(response.status_code, 200)

    def test_men_shoes_page(self):
        """ TC_006: Men's shoes page loads successfully """
        response = self.client.get('/men/shoes')
        self.assertEqual(response.status_code, 200)

    def test_men_accessories_page(self):
        """ TC_007: Men's accessories page loads successfully """
        response = self.client.get('/men/accessories')
        self.assertEqual(response.status_code, 200)

    def test_search_items_name(self):
        """ TC_008: Search bar returns items by item name (dress) """
        response = self.client.get('/search-bar?search=dress')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Vest Dress', response.data)
        self.assertNotIn(b'Checkered Overalls', response.data)

    def test_search_items_color(self):
        """ TC_009: Search bar returns items by color (brown)"""
        response = self.client.get('/search-bar?search=brown')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Vest Dress', response.data)
        self.assertNotIn(b'Checkered Overalls', response.data)

    def test_search_items_category(self):
        """ TC_010: Search bar returns items by category (women)"""
        response = self.client.get('/search-bar?search=women')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Vest Dress', response.data)
        self.assertNotIn(b'String Joggers', response.data)

    def test_search_items_subcategory(self):
        """ TC_011: Search bar returns items by subcategory (accessories)"""
        response = self.client.get('/search-bar?search=accessories')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Freedom Socks', response.data)
        self.assertIn(b'Running Socks', response.data)
        self.assertNotIn(b'String Joggers', response.data)

    def test_search_items_empty(self):
        """ TC_012: Search bar returns nothing if no items found"""
        response = self.client.get('/search-bar?search=fasdjf')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No results found', response.data)

    def test_admin_login_page(self):
        """ TC_017: Login page loads successfully """
        response = self.client.get('/admin/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Admin Login', response.data)

    def test_admin_login_valid(self):
        """ TC_018: Successful login goes to admin page """
        response = self.client.post('/admin/login', data={
            'username': 'admin',
            'password': 'Group11'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Admin Dashboard', response.data)

    def test_admin_login_invalid_password(self):
        """ TC_019: Invalid password login shows invalid credentials message """
        response = self.client.post('/admin/login', data={
            'username': 'admin',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid credentials', response.data)

    def test_admin_login_invalid_password(self):
        """ TC_020: Invalid username login shows invalid credentials message """
        response = self.client.post('/admin/login', data={
            'username': 'username',
            'password': 'Group11'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid credentials', response.data)

    def test_add_item_to_cart(self):
        """ TC_013: Add item to shopping cart and check if stored in session """
        with self.client as client:
            with client.session_transaction() as sess:
                sess['shopping_cart'] = []  # Empty cart

            client.post('/add_to_cart', data={'item_id': '000001'}, follow_redirects=True)

        with client.session_transaction() as sess:
            self.assertIn('shopping_cart', sess)
            self.assertEqual(len(sess['shopping_cart']), 1)
            self.assertEqual(sess['shopping_cart'][0]['id'], '000001')
            self.assertEqual(sess['shopping_cart'][0]['quantity'], 1)

    def test_add_same_item_twice_to_cart(self):
        """ TC_014: Add the same item twice and check quantity increments """
        with self.client as client:
            with client.session_transaction() as sess:
                sess['shopping_cart'] = []

        client.post('/add_to_cart', data={'item_id': '000001'}, follow_redirects=True)
        client.post('/add_to_cart', data={'item_id': '000001'}, follow_redirects=True)

        with client.session_transaction() as sess:
            self.assertEqual(len(sess['shopping_cart']), 1)
            self.assertEqual(sess['shopping_cart'][0]['id'], '000001')
            self.assertEqual(sess['shopping_cart'][0]['quantity'], 2)

    def test_shopping_cart_page(self):
        """ TC_015: Shopping cart page loads and displays added items correctly """
        with self.client as client:
            with client.session_transaction() as sess:
                sess['shopping_cart'] = [{'id': '000001', 'quantity': 2}]

        response = client.get('/shopping-cart')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Checkered Overalls', response.data)  
        self.assertIn(b'2', response.data)  


if __name__ == '__main__':
    unittest.main()