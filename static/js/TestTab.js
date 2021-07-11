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
