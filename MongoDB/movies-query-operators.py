import pymongo
import pprint

//Replace XXXX with your connection URI from the Atlas UI
mc = pymongo.MongoClient("XXXX")
mflix = mc['mflix']

//find all movies released from 1983 onwards
filters = {'year': { '$gte': 1983 }}

for movie in mflix.movies.find(filters):
    pprint.pprint(movie['title'])

//find all movies between 1989 and 1999
filters = { 'year': {'$gte': 1989, '$lt': 2000} }

for movie in mflix.movies.find(filters):
    pprint.pprint(movie['title'])

//find all movies released in 1995, 2005, 2015
filters = { 'year': { '$in': [ 1995, 2005, 2015 ] } }
for movie in mflix.movies.find(filters):
    pprint.pprint(movie['title'])

//find all movies except the ones which are of adult genre
filters = { 'year': { '$in': [ 1995, 2005, 2015 ] }, 
                     'genre': { '$not' : {'$eq': 'Adult'} } }

for movie in mflix.movies.find(filters):
    pprint.pprint(movie['title'])

