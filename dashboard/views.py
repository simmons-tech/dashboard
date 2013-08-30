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

from django.template import RequestContext
from django.shortcuts import render_to_response, render
import requests

def home(request):
	class Slide():
		def __init__(self, slide_type, path="NA"):
			# slide_type is of WIDGET or POSTER
			self.stype = slide_type
			self.path = path

	slides = []
	img_urls = requests.get("https://adat.scripts.mit.edu:444/www/dev/simmons/display/dashboard.php").json()

	# naively insert a widget slide after every 2 images
	for i in range(len(img_urls)):
		if i % 2:
			slides.append(Slide("WIDGET"))
		slides.append(Slide("POSTER", img_urls[i]))
	slides.append(Slide("PACKAGE-LIST"))

	return render(request, "index.html", {"slides": slides})

def sevenk(request):
    return render_to_response('sevenk.html', context_instance = RequestContext(request))
