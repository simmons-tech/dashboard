// Generated by CoffeeScript 1.6.1

/* About
*/


/* License and Warranty
*/


(function() {

  $(function() {
    return (function() {
      var d, days, dom, dow, hour, minute, month, months, second;
      d = new Date();
      hour = d.getHours();
      if (hour > 12) {
        hour -= 12;
      }
      minute = d.getMinutes();
      second = d.getSeconds();
      if (minute < 10) {
        minute = "0" + minute;
      }
      $('#time h1').html("" + hour + ":" + minute);
      dow = d.getDay();
      days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
      dow = days[dow];
      dom = d.getDate();
      month = d.getMonth();
      months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'];
      month = months[month];
      $('#time h2').html("" + dow + ", " + month + " " + dom);
      return setTimeout(arguments.callee, 60000);
    })();
  });

}).call(this);
