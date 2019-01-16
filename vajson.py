import json
from verbs import *
from adjectives import *

# This script creates verb and adjective dictionaries
# and stores them in seperate json files

vdict = verbs()  # initializes verb dictionary
vjson = json.dumps(vdict)  # convert verb dictionary to json string

adict = adjectives()  # initialize adjective dictionary
ajson = json.dumps(adict)  # convert adjective dictionary to json string

with open('verbs.json', 'w') as v:  # writes json string to file
    json.dump(vjson, v, indent=4)  # indent supposed to desquish but it isnt working

with open('adjectives.json', 'w') as a:  # writes json string to file
    json.dump(ajson, a, indent=4)  # indent supposed to desquish but it isnt working
