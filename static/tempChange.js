/**
 * Created by Tim Mui on 12/8/2014.
 */
function tempChange() {
    var u1, u2;
    var x, output;

    // Get the value of input field with id="numb"
    x = document.getElementById("tempInput").value.trim();
    u1 = document.getElementById("unit1").value;
    u2 = document.getElementById("unit2").value;

    if (isNaN(x) == true || x == ""){
        return false;
    }
    else if (isNaN(x) == false){
        // Celsius
        if (u1 == "c") {
            if (u2 == "c") {
                output = x + " °C";
            }
            else if (u2 == "k") {
                output = (parseFloat(x) + 273.15) + " K";
            }
            else if (u2 == "f") {
                output = toF(x) + " °F";
            }
            else if (u2 == "r") {
                output = (toF(x) + 459.67) + " °R";
            }
        }
        // Kelvin
        if (u1 == "k") {
            if (u2 == "c") {
                output = (parseFloat(x) - 273.15) + " °C";
            }
            else if (u2 == "k") {
                output = x + " K";
            }
            else if (u2 == "f") {
                output = toF(parseFloat(x) - 273.15) + " °F";
            }
            else if (u2 == "r") {
                output = (toF(parseFloat(x) - 273.15) + 459.67) + " °R";
            }
        }
        // Fahrenheit
        if (u1 == "f") {
            if (u2 == "c") {
                output = toC(x) + " °C";
            }
            else if (u2 == "k") {
                output = (parseFloat(toC(x)) + 273.15) + " K";
            }
            else if (u2 == "f") {
                output = x + " °F";
            }
            else if (u2 == "r") {
                output = (parseFloat(x) + 459.67) + " °R";
            }
        }
        // Rankine
        if (u1 == "r") {
            if (u2 == "c") {
                output = toC(parseFloat(x) - 459.67) + " °C";
            }
            else if (u2 == "k") {
                output = (parseFloat(toC(parseFloat(x) - 459.67)) + 273.15) + " K";
            }
            else if (u2 == "f") {
                output = (parseFloat(x) - 459.67) + " °F";
            }
            else if (u2 == "r") {
                output = x + " °R";
            }
        }
    }
    return false;
}
// Celsius to Fahrenheit
function toF (num){
    return ((9.0/5)*num+32);
}

// Fahrenheit Celsius
function toC (num){
    return (5*(num-32)/9.0);
}

