### About #####################################################################
#                                                                             #
# This code is part of the Simmons Hall Dashboard project. An up-to-date      #
# version can be found at https://github.com/simmons-tech/dashboard .         #
#                                                                             #
# The project is built an maintained by Simmons Tech, a student organization  #
# at MIT. The original code was produced by Luke O'Malley '14 and             #
# Will Oursler '15                                                            #
#                                                                             #
### License and Warranty ######################################################
#                                                                             #
# Copyright 2013 Simmons Hall                                                 #
#                                                                             #
# Licensed under LGPL3 (the "License"). You may not use this work except in   #
# compliance with the License. You may obtain a copy of the License at        #
# http://opensource.org/licenses/lgpl-3.0.html .                              #
#                                                                             #
# Unless required by applicable law or agreed to in writing, software         #
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT   #
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.            #
###############################################################################

$ ->
	doc = document
	ctr = 0
	spaces = /\s+/
	a1 = [""]
	toArray = (list) ->
		Array::slice.call list or [], 0

	byId = (id) ->
		# If we see that we've got a string, get the associated element.
		return doc.getElementById(id) if typeof id is "string"
		# Otherwise, assume we've been passed that element already.
		return id

	query = (query, root) ->
		queryAll(query, root)[0]

	queryAll = (query, root) ->
		return [] unless query
		return toArray(query) unless typeof query is "string"
		if typeof root is "string"
			root = byId(root)
			return [] unless root
		root = root or document
		rootIsDoc = (root.nodeType is 9)
		doc = (if rootIsDoc then root else (root.ownerDocument or document))
		
		# rewrite the query to be ID rooted
		if not rootIsDoc or (">~+".indexOf(query.charAt(0)) >= 0)
			root.id = root.id or ("qUnique" + (ctr++))
			query = "#" + root.id + " " + query
		
		# don't choke on something like ".yada.yada >"
		query += " *" if ">~+".indexOf(query.slice(-1)) >= 0
		toArray doc.querySelectorAll(query)

	strToArray = (s) ->
		if typeof s is "string" or s instanceof String
			if s.indexOf(" ") < 0
				a1[0] = s
				return a1
			else
				return s.split(spaces)
		s


	# Needed for browsers that don't support String.trim() (e.g. iPad)
	trim = (str) ->
		str.replace(/^\s\s*/, "").replace /\s\s*$/, ""

	addClass = (node, classStr) ->
		classStr = strToArray(classStr)
		cls = " " + node.className + " "
		i = 0
		len = classStr.length
		c = undefined

		while i < len
			c = classStr[i]
			cls += c + " " if c and cls.indexOf(" " + c + " ") < 0
			++i
		node.className = trim(cls)

	removeClass = (node, classStr) ->
		cls = undefined
		if classStr isnt `undefined`
			classStr = strToArray(classStr)
			cls = " " + node.className + " "
			i = 0
			len = classStr.length

			while i < len
				cls = cls.replace(" " + classStr[i] + " ", " ")
				++i
			cls = trim(cls)
		else
			cls = ""
		node.className = cls unless node.className is cls


	#
	# Slide class
	#
	Slide = (name) ->
		@_name = name
		addClass @_name, "slide waiting"

	Slide:: =
		_name: null
		_states: ["previous", "current", "next", "waiting"]
		setState: (state) ->
			removeClass @_name, @_states
			addClass @_name, state


	#
	# SlideShow class
	#
	SlideShow = (slides) ->
		@slides = (slides or []).map((el) ->
			new Slide(el)
		)
		_t = this
		document.addEventListener "keydown", ((e) ->
			_t.handleKeys e
		), false
		@update()

	SlideShow:: =
		slides: []
		update: ->
			i = 0

			while i < @slides.length
				@slides[i].setState "waiting"
				i++
			@slides[@slides.length - 1].setState "previous"
			@slides[1].setState "next"
			@slides[0].setState "current"

		next: ->
			@slides.push @slides.shift()
			@update()

		prev: ->
			@slides.unshift @slides.pop()
			@update()

		handleKeys: (e) ->
			switch e.keyCode
				when 37 # left arrow
					@prev()
				when 39 # right arrow
					@next()

	slideshow = new SlideShow(queryAll('.slide'))
	next = () ->
		slideshow.next()
		setTimeout(arguments.callee, 15000)
	next()
