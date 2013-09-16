### About #####################################################################
#                                                                             #
# This code is part of the Simmons Hall Dashboard project. An up-to-date      #
# version can be found at https://github.com/simmons-tech/dashboard .         #
#                                                                             #
# The project is built an maintained by Simmons Tech, a student organization  #
# at MIT. The original code was produced by Luke O'Malley '14 and             #
# Will Oursler '15                                                            #
#                                                                             #
### License and Warranty ######################################################
#                                                                             #
# Copyright 2013 Simmons Hall                                                 #
#                                                                             #
# Licensed under LGPL3 (the "License"). You may not use this work except in   #
# compliance with the License. You may obtain a copy of the License at        #
# http://opensource.org/licenses/lgpl-3.0.html .                              #
#                                                                             #
# Unless required by applicable law or agreed to in writing, software         #
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT   #
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.            #
###############################################################################

$ ->
		(->
			d = new Date()
			hour = d.getHours()
			# 12 hour clock
			if hour > 12
				hour -= 12
			minute = d.getMinutes()
			second = d.getSeconds()

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

			setTimeout arguments.callee, 60000
		)()
