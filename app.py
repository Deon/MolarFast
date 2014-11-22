__author__ = 'Owner'
from flask import *
import os
import logic

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/getTime")
def getTime():
    return logic.getTime()

if __name__ == ("__main__"):
    app.run(debug=True,host='127.0.0.1',port=int(os.environ.get("PORT", 5000)))