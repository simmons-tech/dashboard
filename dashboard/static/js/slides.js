	var doc = document;

	var ctr = 0;
	var spaces = /\s+/, a1 = [''];

	var toArray = function(list) {
		return Array.prototype.slice.call(list || [], 0);
	};

	var byId = function(id) {
		if (typeof id == 'string') { return doc.getElementById(id); }
		return id;
	};

	var query = function(query, root) {
		return queryAll(query, root)[0];
	}

	var queryAll = function(query, root) {
		if (!query) { return []; }
		if (typeof query != 'string') { return toArray(query); }
		if (typeof root == 'string') {
			root = byId(root);
			if(!root){ return []; }
		}

		root = root || document;
		var rootIsDoc = (root.nodeType == 9);
		var doc = rootIsDoc ? root : (root.ownerDocument || document);

		// rewrite the query to be ID rooted
		if (!rootIsDoc || ('>~+'.indexOf(query.charAt(0)) >= 0)) {
			root.id = root.id || ('qUnique' + (ctr++));
			query = '#' + root.id + ' ' + query;
		}
		// don't choke on something like ".yada.yada >"
		if ('>~+'.indexOf(query.slice(-1)) >= 0) { query += ' *'; }
		return toArray(doc.querySelectorAll(query));
	};

	var strToArray = function(s) {
		if (typeof s == 'string' || s instanceof String) {
			if (s.indexOf(' ') < 0) {
				a1[0] = s;
				return a1;
			} else {
				return s.split(spaces);
			}
		}
		return s;
	};

	// Needed for browsers that don't support String.trim() (e.g. iPad)
	var trim = function(str) {
		return str.replace(/^\s\s*/, '').replace(/\s\s*$/, '');
	};

	var addClass = function(node, classStr) {
		classStr = strToArray(classStr);
		var cls = ' ' + node.className + ' ';
		for (var i = 0, len = classStr.length, c; i < len; ++i) {
			c = classStr[i];
			if (c && cls.indexOf(' ' + c + ' ') < 0) {
				cls += c + ' ';
			}
		}
		node.className = trim(cls);
	};

	var removeClass = function(node, classStr) {
		var cls;
		if (classStr !== undefined) {
			classStr = strToArray(classStr);
			cls = ' ' + node.className + ' ';
			for (var i = 0, len = classStr.length; i < len; ++i) {
				cls = cls.replace(' ' + classStr[i] + ' ', ' ');
			}
			cls = trim(cls);
		} else {
			cls = '';
		}
		if (node.className != cls) {
			node.className = cls;
		}
	};

	var toggleClass = function(node, classStr) {
		var cls = ' ' + node.className + ' ';
		if (cls.indexOf(' ' + trim(classStr) + ' ') >= 0) {
			removeClass(node, classStr);
		} else {
			addClass(node, classStr);
		}
	};

	//
	// Slide class
	//
	var Slide = function(node) {
		this._node = node;
		if (this._node) {
			addClass(this._node, 'slide distant-slide');
		}
	};

	Slide.prototype = {
		_node: null,
		_currentState: '',
		_states: [ 'distant-slide', 'far-past',
							 'past', 'current', 'future',
							 'far-future', 'distant-slide' ],
		setState: function(state) {
			if (typeof state != 'string') {
				state = this._states[state];
			}
			removeClass(this._node, this._states);
			addClass(this._node, state);
			this._currentState = state;
		},

	};

	//
	// SlideShow class
	//
	var SlideShow = function(slides) {
		this._slides = (slides || []).map(function(el) {
			return new Slide(el);
		});

		this.current = "landing-slide";

		var _t = this;
		document.addEventListener('keydown', function(e) { _t.handleKeys(e); }, false);
	
		this._update();
	};

	SlideShow.prototype = {
		_slides: [],
		_getCurrentIndex: function() {
			var _t = this;
			var slideCount = null;
			queryAll('.slide').forEach(function(slide, i) {
				if (slide.id == _t.current) {
					slideCount = i;
				}
			});
			return slideCount + 1;
		},
		_update: function(targetId) {
			// in order to delay the time where the counter shows the slide number we check if
			// the slides are already loaded (so we show the loading... instead)
			// the technique to test visibility is taken from here
			// http://stackoverflow.com/questions/704758/how-to-check-if-an-element-is-really-visible-with-javascript
			var currentIndex = this._getCurrentIndex();

			if (targetId) {
				var savedIndex = currentIndex;
				this.current = targetId;
				currentIndex = this._getCurrentIndex();
				if( Math.abs(savedIndex - currentIndex) > 1 ) {
					// if we're jumping more than one slide for some reason,
					// we need to clean up so that slides won't persist.
					for (var x = savedIndex - 4; x < savedIndex + 3; x++) {
						if (this._slides[x]) {
							this._slides[x].setState( 'distant-slide' );
						}
					}
				}
			}
			
			for (var x = currentIndex - 4; x < currentIndex + 3; x++) {
				if (this._slides[ x ]) {
					this._slides[ x ].setState(x + 4 - currentIndex);
				}
			}
		},

		current: 0,
		next: function() {
			var next = query('#' + this.current + ' + .slide');
			this._update((next) ? next.id : this.current);
		},
		prev: function() {
			var prev = query('.slide:nth-child(' + (this._getCurrentIndex()) + ')');
			this._update((prev) ? prev.id : this.current);
		},

		handleKeys: function(e) {
			switch (e.keyCode) {
				case 37: // left arrow
					this.prev(); break;
				case 39: // right arrow
					this.next(); break;
			}
		},
	};

	var slideshow = new SlideShow(queryAll('.slide'));

