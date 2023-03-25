from contextlib import _RedirectStream
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/booking", methods=['GET','POST'])
def booking():
    
    return render_template('booking.html')

@app.route("/seatbook")
def seatbook():
    return render_template('seatbook.html')


@app.route("/confirm")
def confirm():
    return render_template('confirm.html')




app.run(debug=True)