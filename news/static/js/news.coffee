$ ->
	(->
		$.get('/news', (news) ->
			$('#news .title').html(news.title)
		)
		# Run every 10 seconds
		setTimeout arguments.callee, 10000
	)()
