(function (){
    'use strict';
    var app = angular.module('app');

    app.controller('recipeController', ['$scope', '$http', recipeController]);
    console.log("recipeController initialized");

    function recipeController($scope, $http) {
        console.log("recipeController initialized");
        var baseUrl = 'http://0.0.0.0:8000/';

        $scope.search = function () {
            console.log($scope.ingredients);
        }

        $scope.listen = function () {
            console.log("listening ...");
        }
    };

}());
