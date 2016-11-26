// karma.conf.js
module.exports = function(config) {
  config.set({
    basePath: '.',
    frameworks: ['jasmine'],

    files: [
      "static/js/src/**/*.js",
      "static/js/test/**/*.js"
    ],

    preprocessors: {
      "static/js/src/**/*.js": ["babel"],
      "static/js/test/**/*.js": ["babel"]
    },

    browsers: ['Firefox']
  });
};