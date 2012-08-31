from django.http import HttpResponse
import json
import feedparser

def getTopStories(request):
    # Chose BBC for now, but should include others in the future
    # Consider adding stock ticker here too
    bbcWorldRSS = 'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/front_page/rss.xml'

    # News array
    news = []
    for entry in feedparser.parse(bbcWorldRSS).entries:
        story = { 'title': entry.title,
                  'summary': entry.summary,}
        news.append(story)

    jsonout = json.dumps(news)
    
    return HttpResponse(jsonout, mimetype="application/json")
