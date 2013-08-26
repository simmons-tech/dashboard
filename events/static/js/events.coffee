$ ->
	(->
		$.get('/events', (event) ->
			$('#events .title').html(event.title)
			$('#events .time').html(event.time)
		)
		
		# Run every 15 seconds
		setTimeout arguments.callee, 15000
	)()
