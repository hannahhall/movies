'use strict';
var webpack = require('webpack'),
path = require('path');

var APP = __dirname;

module.exports = {
  context: APP,
   entry: {
         app: './search_app/static/src/javascript/index.js'
  },
  output: {
      path: './search_app/static/dist/',
      filename: 'bundle.js'
  }
};
