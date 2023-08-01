from flask import Flask, render_template, request
import smtplib
import datetime as dt
import random

MY_EMAIL = "affan.works31@gmail.com"
MY_PASSWORD = "ripulmgqsuyhybju"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs='affan.abid99@gmail.com',
            msg=f"Subject:Message\n\nName: {name}\nEmail: {email}\nMessage: {message}"
    )
    return f'<h1><b>success</b></h1>'

if __name__ == '__main__':
    app.run(debug=True)