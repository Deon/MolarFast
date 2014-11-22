/**
 * Created by Owner on 11/21/2014.
 */

//Declare module
var app = angular.module('CoopFriend', ['ui.bootstrap']);

app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
})

.controller('MainCtrl', function($scope, $http) {

    }