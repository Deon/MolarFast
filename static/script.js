/**
 * Created by Owner on 11/21/2014.
 */

//Declare module
var app = angular.module('FirstYear', ['ui.bootstrap']);

app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
})

.controller('MainCtrl', function($scope, $http){

        $scope.displayDate = function(info){
            $http({
                url: "/getTime",
                headers: {'Content-Type': 'application/json'}
            })

                .then(function(time){
                    info.time  = time.data
                }
        }

    }