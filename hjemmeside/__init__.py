from flask import Flask, url_for
from flask import render_template

app = Flask(__name__) #Enten name eller main, det skal være her, for at fortælle siden hvor den skal kigge efter html siden osv.
app.config['SECRET_KEY'] = '172ajqw4qhtyk1bmc43dni4g41objr5s'
app.config['UPLOAD_FOLDER'] = "sarah/server/uploads/"
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}

#Route bliver brugt, til at fortælle hvilken url der skal trigger denne command.
#Kør programmet med: export FLASK_APP=FlaskWebsite.py og efterfølgende: python -m flask run, hvis andre skal kunne joine
#skal den sidste linje hedde: python -m flask run --host=0.0.0.0
#Eller bare run det asnormal

from hjemmeside.server.views.index import IndexView

IndexView.register(app, route_base="/")
