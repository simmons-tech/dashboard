addClass = ( name, state ) ->
	console.log "addClass #{name} #{state}"

removeClass = ( name, states ) ->
	console.log "removeClass #{name} #{states}"

# Slide Class
class Slide

	constructor = ( name ) ->
		@name = name
		@state = 'waiting'
		@setState( @state )

	# List of all the states we're going to use.
	states: [ 'prev', 'current', 'next', 'waiting' ]

	# Sets the "state" of the slide.
	# (Forces the class of the div to the state).
	setState: ( state ) ->
		removeClass( @name, @states )
		addClass( @name, state )
		@state = state

# SlideShow class
class SlideShow

	constructor: ( slides ) ->
		@slides = slides
		# TODO Handle keys, touch, etc?
		_t = this
		document.addEventListener('keydown', (e) ->
				_t.handleKeys(e)
		, false)
		@update()

	update: ->

		# If at least one slide needs to be set to waiting, do that.
		if( @slides.length > 3 )
			for i in [ 0..@slides.length ]
				@slides[ 0 ].setState( "waiting" )

		# If we have enough slides to set a third slide...
		if( @slides.length > 2 )
			@slides[ @slides.length - 1 ].setState( "prev" )

		# If we have enough slides to need to cycle at all...
		if( @slides.length > 1 )
			@slides[ 1 ].setState( "next" )
		@slides[ 0 ].setState( "current" )

	next: ->
		@slides.push( @slides.shift() )
		@update()

	prev: ->
		@slides.unshift( @slides.pop() )
		@update()

	handleKeys: (e) ->
		switch (e.keyCode)
			when 37 then @prev() # left arrow
			when 39 then @next() # right arrow
