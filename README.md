MolarFast
=========
## About MolarFast
<p>
MolarFast is designed to give you the Molar Mass of a chemical compound quickly - hence MolarFast.
As of the latest update, MolarFast is mostly functional - you can use brackets, coefficents, and hydrates.
Currently, nested brackets are not working.
</p>

On Android devices with Chrome M39 and above, choosing "Add to Homescreen" will add MolarFast to your homescreen, where it will run in a seperate instance. 
Internet is still required.

<p>Most information on constants and other values were obtained from data sheets provided by the
University of Waterloo Department of Chemical Engineering. Standard atomic weight is used for all molar mass calculations. Standard atomic weight values
were obtained from <a href="http://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl">National Institute of Standards and Technology (NIST)</a>.
The University of Waterloo, University of Waterloo Department of Chemical Engineering, nor NIST is associated or affiliated with MolarFast.</p>

<p>This web-app was developed with AngularJS, Bootstrap, Flask, and Python.</p>

<p>MolarFast is published under the <a href = "http://www.gnu.org/copyleft/gpl.html">GNU GPL v3.0 Licence.</a></p>



### About Us

MolarFast was created at SE Hack Day #13 on November 21, 2014 by
<a href = "http://github.com/timmui">Timothy Mui</a>, a Computer Engineering student,
and <a href = "http://github.com/DeonHua">Deon Hua</a>, a Software Engineering student.

Made with love.

## Development
Simply clone the repo, install flask and flask-cors via PIP, and run `app.py`. 

### API Endpoint
Send a POST request to `postChemFormula`, with `{{formula:"yourChemFormula"}}`. The molar mass will be returned.
