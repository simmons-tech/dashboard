$ ->
	# Syntactic sugar, really. Create a function to make reloading easy...
	reload = ->
		location.reload( true )
	# Call it an hour after pageload.
	setTimeout reload, 3600000
