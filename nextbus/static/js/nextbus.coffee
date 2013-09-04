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
		$.get('/nextbus', (response) ->
			if response.buses.length is 0
				$("#nextbus .next").html("&Oslash;")
				$("#nextbus .second").html("No")
				$("#nextbus .third").html("Buses")
			else
				if response.buses[0].time_till is "0"
					$("#nextbus .next").html("Now")
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
		setTimeout( arguments.callee, 15000 )
	)()
