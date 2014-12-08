__author__ = 'Deon Hua and Timothy Mui'
from flask import *
import os
import MolarMass

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/conversion.html")
def conversion():
    return render_template("conversion.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/postChemFormula", methods = ["POST"])
def postChemFormula():
    post = request.get_json()
    app.logger.debug(post)
    formula = post.get('formula')
    app.logger.debug(formula)
    molarMass = MolarMass.get_molar_mass(formula)
    if molarMass:
        outputMolarMass = "%.2f" %molarMass
        app.logger.debug(outputMolarMass)
        return outputMolarMass
    else:
        return ""

if __name__ == ("__main__"):
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get("PORT", 5000)))