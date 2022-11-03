import flask
from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
app = flask.Flask(__name__)
app.config["DEBUG"] = True
import requests  # used for testing 
import random
nbateam_data = []
nbateam_list = [
    "NBA",
    "Philadelphia 76ers",
    "Milwaukee Bucks",
    "Boston Celtics",
    "Miami Heat",
    "LA Clippers",
    "LA Lakers",
    "OKC Thunder",
    "Brooklyn Nets",
    "Minnesota Timberwolves",
    "Golden State Warriors",
    "Phoenix Suns",
    "Chicago Bulls",
    "Orlando Magic",
    "Dallas Mavericks",
    "San Antonio Spurs",
    "Atlanta Hawks",
    "Washington Wizards",
    "Houston Rockets",
    "Sacramento Kings",
    "Indiana Pacers",
    "Utah Jazz",
    "New Orleans Pelicans",
    "New York Knicks",
    "Memphis Grizzlies",
    "Portland Trailblazers",
    "Toronto Raptors",
    "Cleveland Cavaliers",
    "Denver Nuggets",
    "Charlotte Hornets",
    "Detroit Pistons",
    
]

def test_text():
    nbateam_data
def test_team():
    nbateam_data

# Initialize nbateams
def nbateams():
    # setup nbateam into a dictionary with team, info, next
    item_id = 0
    for item in nbateam_list:
        nbateam_data.append({"id": item_id, "team": item, "like": 0, "dislike": 0})
        item_id += 1
    # prime some next responses
    for i in range(200):
        id = getRandomnbateam()['id']
        addnbateamlike(id)
    # prime some next responses
    for i in range(50):
        id = getRandomnbateam()['id']
        addnbateamlike(id)
        
# Return all jokes from nbateam_data
def getnbateam():
    return(nbateam_data)

# nbateam getter
def getnbateam(id):
    return(nbateam_data[id])

# Return next team from nbateam_data
def getRandomnbateam():
    return(random.choice(nbateam_data))

# Liked nbateam
def likednbateam():
    best = 0
    bestID = -1
    for id in getnbateam():
        if id['like'] > best:
            best = id['like']
            bestID = id['team']

    return nbateam_data[bestID]
    
#  Disliked nbatam
def dislikednbateam():
    worst = 0
    worstID = -1
    for id in getnbateam():
        if id['dislike'] > worst:
            worst = id['dislike']
            worstID = id['id']
    return nbateam_data[worstID]

# Add to like for requested id
def addnbateamlike(id):
    nbateam_data[id]['like'] = nbateam_data[id]['like'] + 1
    return nbateam_data[id]['like']

# Add to dislike for requested id
def addnbateamlike(id):
    nbateam_data[id]['dislike'] = nbateam_data[id]['dislike'] + 1
    return nbateam_data[id]['dislike']

# Pretty Print nbateam
def printnbateam(nbateam):
    print(nbateam['id'], nbateam['team'], "\n", "like:", nbateam['like'], "\n", "dislike:", nbateam['dislike'], "\n")

# Number of teams  
def countnbateams():
    return len(nbateam_data)

# Test nbateam Model
if __name__ == "__main__": 
    nbateams()  # initialize nbateam

    #  most liked and most disliked
    # best = likednbateam()

    #print("like", best['like'])
    #printnbateam(best)
    # worst = dislikednbateam()
    #print("dislike"), worst['dislike']
    #printnbateam(worst)
    
    # Random team
    
    
       # Random team
    print("Get team 3")
    printnbateam(getnbateam(3))
    
    # Random team
    print("Random team")
    printnbateam(getRandomnbateam())
    
    
    # Count of teams
    printnbateam("team name: " + str(getnbateam()))

 # An input is requested and stored in a variable
nbateam_data = input ("Enter a team: ")

# Converts the string into an integer. If you need
# to convert the user input into the decimal format,
# the float() function is used instead of int()

nbateam_data = int(test_text)

# Prints in the console the variable as requested
printnbateam ("The team you entered is: ", test_team)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/nbateam_list/all', methods=['GET'])
def api_all():
    return jsonify(nbateam_list)

if __name__ == 'main':
    app.run()