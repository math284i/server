from flask_classy import FlaskView, route
from flask import render_template, request, url_for, redirect
#from server.hjemmeside.server.forms import PhotoForm
#from sarah import app
import requests
from bs4 import BeautifulSoup


class IndexView(FlaskView):

    @route('/', methods=['GET', 'POST'])
    def index(self):
        #form = PhotoForm()

        #if form.validate_on_submit():
            #file = form.photo.data

            #print(file.filename, file.content_type)
            #file.save(app.config['UPLOAD_FOLDER'] + file.filename)
        try:
            URL = "https://inside.dtu.dk"
            #URL = "https://www.google.dk/" #<Response [200]>
            page = requests.get(URL) #<Response [200]>
            print(page)
            soup = BeautifulSoup(page.content, 'html.parser')
            return render_template("indexNej.html")
        except:
            return render_template("index.html", )#form=form)

"""request = requests.get('http://www.example.com')
if request.status_code == 200:
    print('Web site exists')
else:
    print('Web site does not exist') """