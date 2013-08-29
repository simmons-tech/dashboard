$ ->
	(->
		$.get('/package_list', (response) ->
			# For now, just print out any response we get.
			console.log(JSON.stringify(response))
			format_person = ( person ) ->
				if person.number > 1
					return person.owner_name + " (x"+person.number+")"
				return person.owner_name
			format_people = ( people ) ->
				s = ""
				s += format_person( person ) + "<br/>" for person in people
				return s
			n = response.people.length
			if n <= 3 * 7
				delta = n / 3
				split1 = delta
				split2 = 2 * delta
				split3 = response.people.length
				more = 0
			else
				split1 = 7
				split2 = 14
				split3 = 20
				more = n - 20
			$('#col1').html(format_people( response.people[0...split1] )) # 8 people max.
			$('#col2').html(format_people( response.people[split1...split2] ))
			if more > 0
				$('#col3').html(format_people( response.people[split2...split3] ) + "(+" + more + " more)")
			else
				$('#col3').html(format_people( response.people[split2...split3] ))
		)

		# Run every 10 seconds (for debug)
		setTimeout arguments.callee, 10000
	)()
