from django.http import HttpResponse
import json

def get_package_list(request):
	people = ["Will Oursler","Caitlin Heber","Cosmos Darwin","Chloe Dlott"]
	return HttpResponse(json.dumps({'people':people}), mimetype="application/json")
