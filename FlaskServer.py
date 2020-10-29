from flask import Flask, url_for
from flask import render_template
app = Flask(__name__) #Enten name eller main, det skal være her, for at fortælle siden hvor den skal kigge efter html siden osv.

#Route bliver brugt, til at fortælle hvilken url der skal trigger denne command.
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello1():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

#Kør programmet med: export FLASK_APP=FlaskWebsite.py og efterfølgende: python -m flask run, hvis andre skal kunne joine
#skal den sidste linje hedde: python -m flask run --host=0.0.0.0
#Eller bare run det asnormal

url_for('static', filename='style.css')

app.run(host='0.0.0.0')

