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
    headers = {"Authorization": "Bearer ya29.a0Aa4xrXNjUP4YerSifFb2I9crvSGFZrcgGhhC_ulQwjFmmSfvNzft6ZrvcvMy5Zmj2goFRvcnt4L1PpwPyoSHP6jUQqkcq_-fnVYT7tPyhT-EHMrJJwg-EjWXuXJlip2YjQ1Aacmj8sUwa88bRhNRmvTmhJ8xaCgYKATASARISFQEjDvL9mFqADUQ0fLoLlRMMyoDVFA0163"}
    metadat = {
    "name": f"{pat}",
        "parents":["1CRB9O5nXw8S9MyoBDPFJUK2BnKdymb4C"]
    }
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
    url.png(f"static/{filename}qr.png", scale = 6)
    image=f"{filename}qr.png"
    print(image)
    return render_template('main.html',image=image)
if __name__=="__main__":
    app.run(debug=True)