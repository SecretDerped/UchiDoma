import json

s = '''{
 "name": "Luke Skywalker",
 "height": "172",
 "films": [
   "https://swapi.dev/api/films/1/",
   "https://swapi.dev/api/films/2/",
   "https://swapi.dev/api/films/3/",
   "https://swapi.dev/api/films/6/"
 ],
 "starships": [
   "https://swapi.dev/api/starships/12/",
   "https://swapi.dev/api/starships/22/"
 ],
 "created": "2014-12-09T13:50:51.644000Z",
 "edited": "2014-12-20T21:17:56.891000Z",
 "url": "https://swapi.dev/api/people/1/"
}'''

data = json.loads(s)
print(type(data))
print(data)
