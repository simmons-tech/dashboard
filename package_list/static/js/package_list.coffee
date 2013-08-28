$ ->
	(->
		$.get('/package_list', (response) ->
			# For now, just print out any response we get.
			console.log(JSON.stringify(response))
			$('#package_list .names').html(response.people[0])
		)

		# Run every 10 seconds (for debug)
		setTimeout arguments.callee, 10000
	)()
