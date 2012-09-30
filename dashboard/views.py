from django.template import RequestContext
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('index.html', context_instance = RequestContext(request))

def sevenk(request):
    return render_to_response('sevenk.html', context_instance = RequestContext(request))
