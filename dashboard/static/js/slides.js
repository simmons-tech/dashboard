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

	//
	// Slide class
	//
	var Slide = function(name) {
		this._name = name;
		addClass(this._name, 'slide waiting');
	};

	Slide.prototype = {
		_name: null,
		_states: [ 'previous', 'current', 'next', 'waiting' ],
		setState: function(state) {
			removeClass(this._name, this._states);
			addClass(this._name, state);
		},

	};

	//
	// SlideShow class
	//
	var SlideShow = function(slides) {
		this.slides = (slides || []).map(function(el) {
			return new Slide(el);
		});

		var _t = this;
		document.addEventListener('keydown', function(e) { _t.handleKeys(e); }, false);
	
		this.update();
	};

	SlideShow.prototype = {
		slides: [],
		update: function() {

			for( var i = 0; i < this.slides.length; i++) {
				this.slides[ i ].setState('waiting')
			}

			this.slides[ this.slides.length - 1 ].setState('previous')
			this.slides[ 1 ].setState('next')
			this.slides[ 0 ].setState('current')
		},
		next: function() {
			this.slides.push( this.slides.shift() );
			this.update();
		},
		prev: function() {
			this.slides.unshift( this.slides.pop() );
			this.update();
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

