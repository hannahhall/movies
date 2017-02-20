angular.module('movie_search', [])
.config(['$interpolateProvider', function($interpolateProvider){
    'use strict';
    $interpolateProvider.startSymbol('[[').endSymbol(']]')
  }])
