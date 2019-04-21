(function (){
    'use strict';
    var app = angular.module('app', []);
    console.log("angular app initialized");

    app.controller('homeController', ['$scope', '$http', homeController]);

    function homeController($scope, $http) {
        console.log("homeController initialized");

        $scope.search = function () {
            var data = {"ingredients": $scope.ingredients}
            console.log(data);
            $http.post('/recipe/search', data)
            .then(function(response) {
                console.log(response.data);
                $scope.recipes = response.data.recipes;
            }
            , function (response) {
                console.log("Unable to find a recipe " + response)
            });
        }

        $scope.listen = function () {
            console.log("listening ...");
            $http.get('/recipe/listen')
            .then(function(response) {
                console.log(response.data);
                $scope.recipes = response.data.recipes;
            }
            , function (response) {
                console.log("Unable to find a recipe " + response)
            });
        }
    };

}());
