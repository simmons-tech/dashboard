$ ->
	(->
		$.get('/nextbus', (bus) ->
			if bus.next is "NA"
				$("#nextbus .next").html("&Oslash;")
				$("#nextbus .second").html("No")
				$("#nextbus .third").html("Buses")
			else
				$("#nextbus .next").html("#{bus.next} min")
				$("#nextbus .second").html("#{bus.second} min")
				$("#nextbus .third").html("#{bus.third} min")
		)

		# Run every 15 seconds
		setTimeout arguments.callee, 15000
	)()
