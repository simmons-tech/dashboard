$ ->
	getTime = ->

		d = new Date()
		hour = d.getHours()
		minute = d.getMinutes()

		hourRotation = (hour * 30) + minute * 0.5 - (minute * 0.5 % 6)
		$(".hour-hand").attr('style', "-webkit-transform: rotate(#{hourRotation}deg);")

		minuteRotation = minute * 6
		$(".minute-hand").attr('style', "-webkit-transform: rotate(#{minuteRotation}deg);")

		# 12 hour clock
		if hour > 12
			hour -= 12

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

		setTimeout(getTime, 5000)

	getTime()
