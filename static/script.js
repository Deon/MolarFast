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

    $scope.findMolarMass = function(model){
        $scope.originalFormula = model;
        console.log($scope.originalFormula);

        if ($scope.originalFormula === null || $scope.originalFormula === undefined || $scope.originalFormula === ""){
            $scope.error = "You should fill it in!";
            $scope.isError = true;
            $scope.originalFormula = null;
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