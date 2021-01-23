from flask import Flask, render_template, url_for
from cs50 import SQL

app = Flask(__name__) #creating a Flask class object   

db = SQL ( "sqlite:///database.db" )

@app.route('/')
def hello():  
    return render_template('home.html')

@app.route('/groceries')
def groceries():
    items = db.execute("SELECT * FROM GROCERY")
    return render_template('items.html',items = items)

@app.route('/food')
def food():
    items = db.execute("SELECT * FROM FOOD")
    return render_template('items.html',items = items)

@app.route('/fruits')
def fruits():
    items = db.execute("SELECT * FROM FRUITS")
    return render_template('items.html',items = items)

@app.route('/stationary')
def stationary():
    items = db.execute("SELECT * FROM STATIONARY")
    return render_template('items.html',items = items)

@app.route('/dairy')
def dairy():
    items = db.execute("SELECT * FROM DAIRY")
    return render_template('items.html',items = items)

@app.route('/crafts')
def crafts():
    items = db.execute("SELECT * FROM CRAFTS")
    return render_template('items.html',items = items)

@app.route('/fashion')
def fashion():
    items = db.execute("SELECT * FROM FASHION")
    return render_template('items.html',items = items)

@app.route('/diwali')
def diwali():
    items = db.execute("SELECT * FROM DIWALI")
    return render_template('items.html',items = items)


if __name__ =='__main__':  
    app.run(debug = True)