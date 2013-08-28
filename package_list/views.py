from django.http import HttpResponse
import json

def get_package_list(request):
	people = ["Will Oursler", "Ashley Villar", "Caitlin Heber","Cosmos Darwin","Chloe Dlott","Allen Park","Nathan Kipniss","Sean Karson","Blah","Blah","Blah","Blah","Blah","Blah","Blah","Blah","Blah","Blah","Blah","Blah"]
	people = [ { 'owner_name':person, 'number':hash(person)%3+1 } for person in people ]
	people[1]['number']=100
	return HttpResponse(json.dumps({'people':people}), mimetype="application/json")
