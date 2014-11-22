__author__ = 'Owner'
from flask import *
import os
import logic
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/getTime/")
def getTime():
    figured = logic.getTime()
    app.logger.debug(figured)
    time = json.dumps(figured)
    return figured

if __name__ == ("__main__"):
    app.run(debug=True,host='127.0.0.1',port=int(os.environ.get("PORT", 5000)))