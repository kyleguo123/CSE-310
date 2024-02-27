import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

cred = credentials.Certificate("stockfile/firebaseapikey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://data-for-stock-69ec3-default-rtdb.firebaseio.com/'
})

# Reference to the root of your Firebase Realtime Database
ref = db.reference()

def update_stock_price(stock_price):
    global ref
    # Retrieve data from the database
    # data = ref.get()
    # if data["stock_price"] != stock_price:
    ref.update({"stock_price":stock_price})

def undate_interest_percentage(interest):
    global ref

    ref.update({"Percentage":interest})

def undate_chart(stock_data):
    global ref

    ref.update({"stock_data":stock_data})