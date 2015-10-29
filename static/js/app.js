'use strict';

(function(){
  // Declare app level module which depends on views, and components
  var app = angular.module('FlagConsole', []);

  app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  });

  app.controller('SystemsController', ['$http', function($http){
    var controller = this;
    controller.systems = [];

    $http.get('/api/systems').then(function success(response) {
      controller.systems = response.data.results;
    }, function error(response) {
      alert("Request for /api/systems returned status " + response.status + ".");
    });
  }]);

  app.controller('ApplicationsController', ['$http', function($http){
    var controller = this;
    controller.system = null;
    controller.applications = [];

    controller.setSystem = function(system) {
      controller.system = system;
      var url = '/api/apps/' + system;

      $http.get(url).then(function success(response) {
        controller.applications = response.data.results;
      }, function error(response) {
        alert("Request for " + url + " returned status " + response.status + ".");
      });
    };

    controller.systemText = function() {
      return controller.system === null ? "System" : controller.system;
    };
  }]);

  app.controller('FlagsController', ['$http', function($http){
    var controller = this;
    controller.system = null;
    controller.application = null;
    controller.flags = [];

    controller.setApplication = function(system, application) {
      controller.system = system;
      controller.application = application;

      if (application == null) {
        controller.flags = [];
      } else {
        var url = '/api/flags/' + system + '/' + application;
        $http.get(url).then(function success(response) {
          controller.flags = response.data.results;
        }, function error(response) {
          alert("Request for " + url + " returned status " + response.status + ".");
        });
      }
    };

    controller.applicationText = function() {
      return controller.application === null ? "Application" : controller.application;
    }
  }]);

  app.filter('renderstatus', function() {
    return function(input) {
      if (input === true) {
        return 'enabled';
      } else if (input === false) {
        return 'disabled';
      } else {
        return 'n/a';
      }
    }
  });

})();
