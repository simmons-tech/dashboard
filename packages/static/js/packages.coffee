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
		$.get('/packages', (response) ->
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
		setTimeout( arguments.callee, 300000 )
	)()
