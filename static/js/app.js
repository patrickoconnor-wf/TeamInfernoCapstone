'use strict';

(function(){
  // Declare app level module which depends on views, and components
  var app = angular.module('FlagConsole', []);

  app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  });

  app.controller('FlagsController', ['$http', function($http){
    this.systems = [];
    this.system = null;
    this.applications = [];
    this.application = null;
    this.flags = [];
    this.searchText = '';
    this.noResults = false;

    $http.get('/api/systems').then(function success(response) {
      controller.systems = response.data.results;
    }, function error(response) {
      alert("Request for /api/systems returned status " + response.status + ".");
    });

    var controller = this;

    this.setSystem = function(system) {
      if (system !== controller.system) {
        controller.system = system;
        controller.applications = [];
        controller.application = null;
        controller.flags = [];
        controller.noResults = false;

        var url = '/api/apps/' + system;
        $http.get(url).then(function success(response) {
          controller.applications = response.data.results;
        }, function error(response) {
          alert("Request for " + url + " returned status " + response.status + ".");
        });
      }
    }

    this.systemText = function() {
      return controller.system === null ? "System" : controller.system;
    };

    this.setApplication = function(application) {
      if (application !== controller.application) {
        controller.application = application;
        controller.flags = [];
        controller.noResults = false;

        var url = '/api/flags/' + controller.system + '/' + application;
        $http.get(url).then(function success(response) {
          controller.flags = response.data.results;
        }, function error(response) {
          alert("Request for " + url + " returned status " + response.status + ".");
        });
      }
    };

    this.applicationText = function() {
      return controller.application === null ? "Application" : controller.application;
    };

    this.appDropdownEnabled = function() {
      return controller.system != null;
    }

    this.search = function() {
      $http.get('/api/search', { params: { q: controller.searchText }}).then(function success(response) {
        controller.system = null;
        controller.application = null;
        controller.flags = response.data.results;
        controller.noResults = response.data.results.length === 0;
      }, function error(response) {
          alert("Request for /api/search returned status " + response.status + ".");
      })
    }

    this.noSearchResults = function() {
      return controller.noResults;
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
