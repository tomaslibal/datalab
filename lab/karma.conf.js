// karma.conf.js
module.exports = function(config) {
  config.set({
    basePath: '.',
    frameworks: ['jasmine', 'requirejs'],

    files: [
      'node_modules/requirejs/require.js',
      'node_modules/karma-requirejs/lib/adapter.js',

      "static/js/build/*.js",
      "static/js/test/**/*.js"
    ],

    preprocessors: {
      "static/js/src/**/*.js": ["babel"],
      "static/js/test/**/*.js": ["babel"]
    },

    browsers: ['Firefox']
  });
};