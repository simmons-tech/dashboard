(function() {

  $(function() {
    var getTime;
    getTime = function() {
      var d, days, dom, dow, hour, hourRotation, minute, minuteRotation, month, months;
      d = new Date();
      hour = d.getHours();
      minute = d.getMinutes();
      hourRotation = (hour * 30) + minute * 0.5 - (minute * 0.5 % 6);
      $(".hour-hand").attr('style', "-webkit-transform: rotate(" + hourRotation + "deg);");
      minuteRotation = minute * 6;
      $(".minute-hand").attr('style', "-webkit-transform: rotate(" + minuteRotation + "deg);");
      if (hour > 12) hour -= 12;
      if (minute < 10) minute = "0" + minute;
      $('#time h1').html("" + hour + ":" + minute);
      dow = d.getDay();
      days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
      dow = days[dow];
      dom = d.getDate();
      month = d.getMonth();
      months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'];
      month = months[month];
      $('#time h2').html("" + dow + ", " + month + " " + dom);
      return setTimeout(getTime, 5000);
    };
    return getTime();
  });

}).call(this);
