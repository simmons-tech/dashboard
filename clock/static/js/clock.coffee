$ ->
	updateHand = (value, total, length, hand) ->
		value -= total while value > total
		if not value or value is total
			value = total
			hand.animate
				hand: [value, total, length], 750, "bounce", ->
				hand.attr hand: [0, total, length]

		else
			hand.animate
				hand: [value, total, length], 750, "elastic"

	container = $('#time #clock');
	container.each (index) ->
		clock = Raphael(container[index], "100%", "100%")
		width = $(clock.canvas.parentElement).width() #TODO: use container somehow?
		height = $(clock.canvas.parentElement).height()
		size = Math.min(width, height)
		param =
			stroke: "#fff"
			"stroke-linecap": "round"

		html = [document.getElementById("h"), document.getElementById("m"), document.getElementById("s")]

		clock.customAttributes.hand = (value, total, length) ->
			alpha = 360 / total * value
			a = (90 - alpha) * Math.PI / 180
			path = [["M", width / 2.0, height / 2.0], ["l", length * Math.cos(a), -1 * length * Math.sin(a)]]
			path: path

		# Lengths...
		second_hand_length = 92.0 * size / 256.0
		minute_hand_length = 90.0 * size / 256.0
		hour_hand_length = 60.0 * size / 256.0

		# Widths...
		surround_width = 7.0 * size / 256.0
		thick_hand_width = 8.0 * size / 256.0
		thin_hand_width = 4.0 * size / 256.0

		# Define the hand objects and the surrounding circle...
		second_hand = clock.path().attr(param).attr(hand: [0, 60, second_hand_length]).attr("stroke-width": thin_hand_width)
		minute_hand = clock.path().attr(param).attr(hand: [0, 60, minute_hand_length]).attr("stroke-width": thick_hand_width)
		hour_hand = clock.path().attr(param).attr(hand: [0, 12, hour_hand_length]).attr("stroke-width": thick_hand_width)
		surround = clock.circle(width / 2.0, height / 2.0, (size - surround_width) / 2.0).attr(param).attr("stroke-width": surround_width)

		# Keep track of the last time we updated ( -1 means that we will update for sure at first. )
		last_hour = -1
		last_minute = -1
		last_second = -1

		(->
			d = new Date()
			hour = d.getHours()
			# 12 hour clock
			if hour > 12
				hour -= 12
			minute = d.getMinutes() % 60
			second = d.getSeconds() % 60

			unless second is last_second
				updateHand second, 60, second_hand_length, second_hand
				last_second = second
			unless minute is last_minute
				updateHand minute, 60, minute_hand_length, minute_hand
				last_minute = minute
			unless hour is last_hour
				updateHand hour, 12, hour_hand_length, hour_hand
				last_hour = hour

			# two digit minute
			if minute < 10
				minute = "0#{minute}"

			$('#time h1').html("#{hour}:#{minute}")

			# day of week
			dow = d.getDay()

			days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

			dow = days[dow]

			dom = d.getDate()

			month = d.getMonth()

			months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

			month = months[month]

			$('#time h2').html("#{dow}, #{month} #{dom}")

			setTimeout arguments.callee, 1000
		)()
