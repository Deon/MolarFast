__author__ = 'Deon Hua and Timothy Mui'
from flask import *
from flask_cors import *
import os
import MolarMass

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def home():
    return render_template("index.html")

#For "Add to Homescreen" for Chrome M39
@app.route("/index.html")
def mobileApp():
    return render_template("index.html")

@app.route("/conversion.html")
def conversion():
    return render_template("conversion.html")


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/google0dec4c879860ede1.html")
def verify():
    return render_template("google0dec4c879860ede1.html")


@app.route("/postChemFormula", methods=["POST"])
@cross_origin()
def postChemFormula():
    post = request.get_json()
    app.logger.debug(post)
    formula = post.get('formula')
    app.logger.debug(formula)
    molarMass = MolarMass.get_molar_mass(formula)
    if molarMass:
        outputMolarMass = "%.3f" %molarMass
        app.logger.debug(outputMolarMass)
        return outputMolarMass
    else:
        return ""

@app.errorhandler(404)
def pageNotFound(error):
    return render_template("pageNotFound.html"), 404


if __name__ == ("__main__"):
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get("PORT", 5000)))