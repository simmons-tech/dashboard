(function() {
  var Slide, SlideShow, addClass, removeClass;

  addClass = function(name, state) {
    return console.log("addClass " + name + " " + state);
  };

  removeClass = function(name, states) {
    return console.log("removeClass " + name + " " + states);
  };

  Slide = (function() {
    var constructor;

    function Slide() {}

    constructor = function(name) {
      this.name = name;
      this.state = 'waiting';
      return this.setState(this.state);
    };

    Slide.prototype.states = ['prev', 'current', 'next', 'waiting'];

    Slide.prototype.setState = function(state) {
      removeClass(this.name, this.states);
      addClass(this.name, state);
      return this.state = state;
    };

    return Slide;

  })();

  SlideShow = (function() {

    function SlideShow(slides) {
      var _t;
      this.slides = slides;
      _t = this;
      document.addEventListener('keydown', function(e) {
        return _t.handleKeys(e);
      }, false);
      this.update();
    }

    SlideShow.prototype.update = function() {
      var i, _ref;
      if (this.slides.length > 3) {
        for (i = 0, _ref = this.slides.length; 0 <= _ref ? i <= _ref : i >= _ref; 0 <= _ref ? i++ : i--) {
          this.slides[0].setState("waiting");
        }
      }
      if (this.slides.length > 2) {
        this.slides[this.slides.length - 1].setState("prev");
      }
      if (this.slides.length > 1) this.slides[1].setState("next");
      return this.slides[0].setState("current");
    };

    SlideShow.prototype.next = function() {
      this.slides.push(this.slides.shift());
      return this.update();
    };

    SlideShow.prototype.prev = function() {
      this.slides.unshift(this.slides.pop());
      return this.update();
    };

    SlideShow.prototype.handleKeys = function(e) {
      switch (e.keyCode) {
        case 37:
          return this.prev();
        case 39:
          return this.next();
      }
    };

    return SlideShow;

  })();

}).call(this);