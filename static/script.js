/**
 * Created by Owner on 11/21/2014.
 */

//Declare module
var app = angular.module('FirstYear', ['ui.bootstrap']);


app.controller('MainCtrl', function($scope, $http){

    $scope.time = "";
    $scope.displayDate = function(){
        $http({
            url: "/getTime"
        })
            .then(function(time){
                $scope.time  = time.data
            }
        )
    };


});