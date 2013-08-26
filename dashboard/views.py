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

	return render(request, "index.html", {"slides": slides})

def sevenk(request):
    return render_to_response('sevenk.html', context_instance = RequestContext(request))
