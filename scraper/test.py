import requests
import json

r = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?query=New%20York&key=AIzaSyDUhlaAXY1VY57HQ4SXuRLD6ZXXp3bFVNE')
json.loads(r.text)

print 'foo'