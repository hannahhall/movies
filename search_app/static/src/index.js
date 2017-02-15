require('./vendor.js')();

angular.module('movie_search', [])
.config(['$interpolateProvider', function($interpolateProvider){
    'use strict';
    $interpolateProvider.startSymbol('[[').endSymbol(']]')
  }])
.controller('HereCtrl', function() {
  alert('loaded!');

  console.log('woohoooooo')

})
