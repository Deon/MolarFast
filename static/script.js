//Activate Tooltips
$(function () { $("[data-toggle='tooltip']").tooltip(); });

//Declare module
var app = angular.module("MolarFast", ['ui.bootstrap']);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

app.controller('MainController', function($scope, $http){

    $scope.time = null;
    $scope.finalMolarMass = null;
    $scope.originalFormula = null;
    $scope.isError = null;

    $scope.findMolarMass = function(model){
        $scope.originalFormula = model;
        console.log($scope.originalFormula);

        if ($scope.originalFormula === null || $scope.originalFormula === undefined || $scope.originalFormula === ""){
            $scope.error = "You should fill it in!";
            $scope.isError = true;
            $scope.originalFormula = null;
            console.log("undefined $scope.input");
        }
        else {
            $http({
                url: '/postChemFormula',
                method: "POST",
                data: JSON.stringify({'formula': model}),
                headers: {'Content-Type': 'application/json'}
            })
              .success(function (molarMass) {
                  if (molarMass === ""){
                      $scope.isError = true;
                      $scope.error = "Check your formula!";
                      console.log("Error in $scope.input.");
                  }
                  else {
                      $scope.finalMolarMass = molarMass;
                      $scope.isError = null;
                  }
                  console.log($scope.finalMolarMass);
              })
              .error(function () {
                  console.log("Error in $scope.input.");
                  $scope.error = "Check your formula!";
                  $scope.finalMolarMass = null;
                  $scope.isError = true;
              });
        }
    };
});

app.controller('ConversionController', function($scope){
    $scope.input = null;
    $scope.firstUnit = "c";
    $scope.secondUnit = "k";
    $scope.output = null;
    $scope.isError = false;

    $scope.tempChange = function () {
        console.log($scope.input);
        if (isNaN($scope.input) == true){
            $scope.isError = true;
        }
        else if ($scope.input == "" || $scope.input == undefined){
            $scope.output = null;
            $scope.isError = false;
        }
        else if (isNaN($scope.input) == false){
            //console.log($scope.firstUnit);
            //console.log($scope.secondUnit);
            $scope.isError = false;
            // Celsius
            if ($scope.firstUnit == "c") {
                if ($scope.secondUnit == "c") {
                    $scope.output = $scope.input + " °C";
                }
                else if ($scope.secondUnit == "k") {
                    $scope.output = (parseFloat($scope.input) + 273.15) + " K";
                }
                else if ($scope.secondUnit == "f") {
                    $scope.output = toF($scope.input) + " °F";
                }
                else if ($scope.secondUnit == "r") {
                    $scope.output = (toF($scope.input) + 459.67) + " °R";
                }
            }
            // Kelvin
            if ($scope.firstUnit == "k") {
                if ($scope.secondUnit == "c") {
                    $scope.output = (parseFloat($scope.input) - 273.15) + " °C";
                }
                else if ($scope.secondUnit == "k") {
                    $scope.output = $scope.input + " K";
                }
                else if ($scope.secondUnit == "f") {
                    $scope.output = toF(parseFloat($scope.input) - 273.15) + " °F";
                }
                else if ($scope.secondUnit == "r") {
                    $scope.output = (toF(parseFloat($scope.input) - 273.15) + 459.67) + " °R";
                }
            }
            // Fahrenheit
            if ($scope.firstUnit == "f") {
                if ($scope.secondUnit == "c") {
                    $scope.output = toC($scope.input) + " °C";
                }
                else if ($scope.secondUnit == "k") {
                    $scope.output = (parseFloat(toC($scope.input)) + 273.15) + " K";
                }
                else if ($scope.secondUnit == "f") {
                    $scope.output = $scope.input + " °F";
                }
                else if ($scope.secondUnit == "r") {
                    $scope.output = (parseFloat($scope.input) + 459.67) + " °R";
                }
            }
            // Rankine
            if ($scope.firstUnit == "r") {
                if ($scope.secondUnit == "c") {
                    $scope.output = toC(parseFloat($scope.input) - 459.67) + " °C";
                }
                else if ($scope.secondUnit == "k") {
                    $scope.output = (parseFloat(toC(parseFloat($scope.input) - 459.67)) + 273.15) + " K";
                }
                else if ($scope.secondUnit == "f") {
                    $scope.output = (parseFloat($scope.input) - 459.67) + " °F";
                }
                else if ($scope.secondUnit == "r") {
                    $scope.output = $scope.input + " °R";
                }
            }
        }
    };

    // Celsius to Fahrenheit
    var toF = function(num){
        return ((9.0/5)*num+32);
    };

    // Fahrenheit Celsius
    var toC = function(num){
        return (5*(num-32)/9.0);
    };
});