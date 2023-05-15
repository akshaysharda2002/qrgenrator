import os
from urllib import request
import pyqrcode
import png
from pyqrcode import QRCode
from flask import Flask
import requests
import json
from flask import render_template,request,flash
app = Flask(__name__)

@app.route("/")
def ho():
    return render_template('main.html',image="default.jpg")
@app.route("/loading", methods=['GET', 'POST'])
def home():
    f = request.files['file']
    filename=f.filename
    f.save(filename)    
    dir=os.path.abspath(os.getcwd())
    pat=os.path.join(dir,filename)
    headers = {"Authorization": "Bearer ya29.a0AWY7Ckmk3oc9dOmcGw7NkhbPoUeEP1hPxb-j9c2u-6YIFOGDPqq8tIO1vI9C2SSWCaJXkf9jU5l-UDXEz2NZGgRriPQi6U9gS5ziL1p0booo7ruLLbGP7qb2rN94UWd8pMWGJ-DYhf1w0jMvP8Wb-AcZU24KaCgYKARoSARISFQG1tDrpa9ZdD0go5amHAR4ZIH0BMg0163"}
    metadat = {"name": "{pat}".format(pat=pat),"parents":["1CRB9O5nXw8S9MyoBDPFJUK2BnKdymb4C"]}
    files = {
    'data': ('metadata', json.dumps(metadat), 'application/json; charset=UTF-8'),
    'file': open(pat, "rb")
    }
    r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
    )
    print(r)
    js=r.json()
    id=js['id']
    link="https://drive.google.com/file/d/{id}/view?usp=sharing".format(id=id)
    url=pyqrcode.create(link)
    url.png("static/{filename}qr.png".format(filename=filename), scale = 6)
    image="{filename}qr.png".format(filename=filename)
    print(image)
    return render_template('main.html',image=image)
if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)