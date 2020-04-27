(function () {
    'use strict';
    var app = angular.module('app', ['webcam']);
    console.log("angular app initialized");

    app.controller('homeController', ['$scope', '$http', homeController]);

    function homeController($scope, $http) {


        console.log("homeController initialized");
        let formData = new FormData();
        $scope.selectFile = function (files) {
            formData.append("image", files[0]);
            $scope.upload();
        };


        $scope.search = function () {
            let ingredients = $scope.ingredients.split(',');
            let data = {"ingredients": ingredients};
            console.log(data);
            $http.post('/recipe/search', data)
                .then(function (response) {
                        console.log(response.data);
                        $scope.recipes = response.data.recipes;
                    }
                    , function (response) {
                        console.log("Unable to find a recipe " + response)
                    });
        };

        $scope.listen = function () {
            console.log("listening ...");
            $http.get('/recipe/listen')
                .then(function (response) {
                        console.log(response.data);
                        $scope.recipes = response.data.recipes;
                        $scope.ingredients = response.data.ingredients;
                    }
                    , function (response) {
                        console.log("Unable to find a recipe " + response)
                    });
        };


        $scope.upload = function () {
            $http.post('/recipe/upload', formData, {
                withCredentials: true,
                headers: {'Content-Type': undefined},
                transformRequest: angular.identity
            })
                .then(function (response) {
                    console.log("SUCCESS");
                    $scope.recipes = response.data.recipes;
                    $scope.ingredients = response.data.ingredients;
                }, function () {
                    console.log("FAILED TO UPLOAD", response);
                })
        };

        $scope.myChannel = {
            // the fields below are all optional
            videoHeight: 800,
            videoWidth: 600,
            video: null // Will reference the video element on success
        };

        $scope.onError = function (err) {
        };
        $scope.onStream = function (stream) {
        };
        $scope.onSuccess = function () {
        };

    }

}());
