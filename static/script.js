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

    $scope.time = "";
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

});