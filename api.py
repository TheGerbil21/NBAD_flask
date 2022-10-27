import random

nbateam_data = []
nbateam_list = [
    "NBA",
    "Phildelphia 76ers",
    "Milluake Bucks",
    "Boston Celtics",
    "Miami Heat",
    "LA Clippers",
    "LA Lakers",
    "OKC Thunder",
    "Brooklyn Nets",
    "Minnesota Timberwolves",
    "Golden State Warriors",
    "Pheonix Suns",
    "Chicago Bulls",
    "Orlando Magic",
    "Dallas Mavricks",
    "San Antonio Spurs",
    "Atlanta Hawks",
    "Washigton Wizards",
    "Housten Rockets",
    "Sacramento Kings",
    "Indiana Pacers",
    "Utah Jazz",
    "New Orleans Pelicans",
    "New York Knicks",
    "Memphis Grizzles",
    "Portland Trailblazers",
    "Toronto Raptors",
    "Cleveland Cavilers",
    "Denver Nuggets",
    "Charolette Hornets",
    "Detroit Pistons",
    
]

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

# Number of jokes
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
    print("Get team 3")
    printnbateam(getnbateam(3))
    
    # Random team
    print("Random team")
    printnbateam(getRandomnbateam())
    
    # Count of teams
    print("team Count: " + str(countnbateams()))
