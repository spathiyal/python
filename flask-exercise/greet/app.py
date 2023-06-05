
from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/welcome')
def welcome():
    html = """
    <html>
     <body> 
     <h1> Welcome</body> </html></body> </html>
     """
    return html

@app.route('/welcome/home')
def welcome_home():
    html = """
    <html>
     <body> 
     <h1> Welcome home</body> </html></body> </html>
     """
    return html

@app.route('/welcome/back')
def welcome_back():
    html = """
    <html>
     <body> 
     <h1> Welcome back</body> </html></body> </html>
     """
    return html