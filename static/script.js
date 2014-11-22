/**
 * Created by Owner on 11/21/2014.
 */

//Declare module
var app = angular.module('FirstYear', []);

app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
})
app.controller('MainCtrl', function($scope, $http){

    $scope.time = null;
    $scope.finalMolarMass = null;

    $scope.displayDate = function(){

        $http({
            url: '/getTime/'
        })
            .then(function(time){
                $scope.time  = time.data;
                console.log($scope.time);
            }
        );
    };

    $scope.testDate = function(){
        $scope.time ='Test time.';
        console.log($scope.time);
    };

    $scope.findMolarMass = function(model){
        if (model == null){
            $scope.error = "You should fill it in!";
        }


        $http({
            url: '/postChemFormula',
            method: "POST",
            data: JSON.stringify({'formula':model}),
            headers: {'Content-Type': 'application/json'}
        })
            .then(function(molarMass){
                $scope.finalMolarMass = molarMass.data;
                console.log($scope.finalMolarMass);
            }
        );
    };

});