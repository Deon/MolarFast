__author__ = 'Owner'
from flask import *
import os
import logic
import json
import MolarMass

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

@app.route("/postChemFormula")
def postChemFormula():
    post = request.get_json()
    app.logger.debug(post)
    formula = post.get()
    molarMass = MolarMass.get_molar_mass(formula)
    app.logger.debug(molarMass)
    return molarMass

if __name__ == ("__main__"):
    app.run(debug=True,host='127.0.0.1',port=int(os.environ.get("PORT", 5000)))