$ ->
	(->
		$.get('/nextbus', (response) ->
			if response.buses.length is 0
				$("#nextbus .next").html("&Oslash;")
				$("#nextbus .second").html("No")
				$("#nextbus .third").html("Buses")
			else
				$("#nextbus .next").html("#{response.buses[0].time_till} min")

				if response.buses.length >= 2
					$("#nextbus .second").html("#{response.buses[1].time_till} min")
				else
					$("#nextbus .second").html("")

				if response.buses.length >= 3
					$("#nextbus .third").html("#{response.buses[2].time_till} min")
				else
					$("#nextbus .third").html("")
		)

		# Run every 15 seconds
		setTimeout arguments.callee, 15000
	)()
