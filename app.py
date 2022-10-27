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
    headers = {"Authorization": "Bearer ya29.a0Aa4xrXPgahu2obdqaI4GeT7oDdLEZx5LupTUG1gf9_YkRNplq_7BYu-9wO5oNebssT2x2ysTFS8-ZLJuZfr37HyME18sqQwh8sAdlY8KS50e0SYfEO9koD3gB-QvErr861b-MBz4wCsW1vwYGTggkJPcKpzmaCgYKATASARMSFQEjDvL9Vjhx3hs8F1cSL5GmNXAGmg0163"}
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
    link=f"https://drive.google.com/file/d/{id}/view?usp=sharing"
    url=pyqrcode.create(link)
    url.png("static/{filename}qr.png".format(filename=filename), scale = 6)
    image="{filename}qr.png".format(filename=filename)
    print(image)
    return render_template('main.html',image=image)
if __name__=="__main__":
    app.run(debug=True)