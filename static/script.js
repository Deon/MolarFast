/**
 * Created by Owner on 11/21/2014.
 */

//Declare module
var app = angular.module('FirstYear', ['ui.bootstrap']);

app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});

app.controller('MainCtrl', function($scope, $http){

    $scope.time = null;
    $scope.finalMolarMass = null;
    $scope.originalFormula = null;
    $scope.isError = null;

    $scope.displayDate = function(){

        $http({
            url: '/getTime/'
        })
            .then(function(time){
                $scope.dateData = time.data;
                console.log($scope.dateData);
                $scope.date = $scope.dateData[0];
                $scope.time = $scope.dateData[1];
            }
        );
    };


    $scope.findMolarMass = function(model){
        $scope.originalFormula = model;
        console.log($scope.originalFormula);

        if ($scope.originalFormula === null || $scope.originalFormula === undefined){
            $scope.error = "You should fill it in!";
            $scope.isError = true;
            console.log("undefined input");
        }
        else {
            $http({
                url: '/postChemFormula',
                method: "POST",
                data: JSON.stringify({'formula': model}),
                headers: {'Content-Type': 'application/json'}
            })
                .success(function (molarMass) {
                    console.log(molarMass);
                    if (molarMass === ""){
                        $scope.isError = true;
                        $scope.error = "Check your formula!";
                        console.log("Error in input.");
                    }
                    else {
                        $scope.finalMolarMass = molarMass;
                        $scope.isError = null;
                    }
                        console.log($scope.finalMolarMass);
                })
                .error(function (molarMass) {
                    console.log("Error in input.");
                    $scope.error = "Check your formula!";
                    $scope.finalMolarMass = null;
                    $scope.isError = true;
                });
        }
    };
});