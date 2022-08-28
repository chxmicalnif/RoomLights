$(function() {
  $('a#turnOn').on('click', function(e) {
    e.preventDefault()
      $.getJSON('/LEDON',
        function(data) {
        // Do nothing
        });
      return false;
    });
});

$(function() {
  $('a#turnOff').on('click', function(e) {
    e.preventDefault()
      $.getJSON('/LEDOFF',
        function(data) {
        // Do nothing
        });
      return false;
    });
});

$(function() {
  $('a#4On').on('click', function(e) {
    e.preventDefault()
      $.getJSON('/4On',
        function(data) {
        // Do nothing
        });
      return false;
    });
});

$(function() {
  $('a#4Off').on('click', function(e) {
    e.preventDefault()
      $.getJSON('/4Off',
        function(data) {
        // Do nothing
        });
      return false;
    });
});

$(function() {
  $('a#kill').on('click', function(e) {
    e.preventDefault()
      $.getJSON('/StopRunning',
        function(data) {
        // Do nothing
        });
      return false;
    });
});

$(function() {
  $('a#writeFile').on('click', function(e) {
    e.preventDefault()
      $.getJSON('/WriteFile',
        function(data) {
        // Do nothing
        });
      return false;
    });
});

$(function() {
  $('a#readFile').on('click', function(e) {
    e.preventDefault()
      $.getJSON('/readFile',
        function(data) {
        // Do nothing
        });
      return false;
    });
});

$(function() {
  $('a#shuffle').on('click', function(e) {
    e.preventDefault()
      $.getJSON('/shuffle',
        function(data) {
        // Do nothing
        });
      return false;
    });
});
