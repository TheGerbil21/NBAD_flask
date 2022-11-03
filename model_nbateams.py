import random
nbateams_data = [
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
    nbateams_data
def test_team():
    nbateams_data

# Initialize nbateams
def initNbateams():
    # setup nbateam into a dictionary with team, info, next
    item_id = 0
    for item in nbateam_list:
        nbateams_data.append({"id": item_id, "team": item, "like": 0, "dislike": 0})
        item_id += 1
    # prime some next responses
    for i in range(200):
        id = getRandomnbateam()['id']
        addnbateamlike(id)
    # prime some next responses
    for i in range(50):
        id = getRandomnbateam()['id']
        addnbateamlike(id)

    print(nbateams_data)
        
# Return all jokes from nbateam_data
def getnbateams():
    return(nbateams_data)

# nbateam getter
def getnbateam(id):
    return(nbateams_data[id])

# Return next team from nbateam_data
def getRandomnbateam():
    return(random.choice(nbateams_data))

# Liked nbateam
def likednbateam():
    best = 0
    bestID = -1
    for id in getnbateam():
        if id['like'] > best:
            best = id['like']
            bestID = id['team']

    return nbateams_data[bestID]
    
#  Disliked nbatam
def dislikednbateam():
    worst = 0
    worstID = -1
    for id in getnbateam():
        if id['dislike'] > worst:
            worst = id['dislike']
            worstID = id['id']
    return nbateams_data[worstID]

# Add to like for requested id
def addnbateamlike(id):
    nbateams_data[id]['like'] = nbateams_data[id]['like'] + 1
    return nbateams_data[id]['like']

# Add to dislike for requested id
def addnbateamdislike(id):
    nbateams_data[id]['dislike'] = nbateams_data[id]['dislike'] + 1
    return nbateams_data[id]['dislike']

# Pretty Print nbateam
def printnbateam(nbateam):
    print(nbateam['id'], nbateam['team'], "\n", "like:", nbateam['like'], "\n", "dislike:", nbateam['dislike'], "\n")

# Number of teams  
def countnbateams():
    return len(nbateams_data)

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
# nbateams_data = input ("Enter a team: ")

# # Converts the string into an integer. If you need
# # to convert the user input into the decimal format,
# # the float() function is used instead of int()

# nbateams_data = int(test_text)

# # Prints in the console the variable as requested
# printnbateam ("The team you entered is: ", test_team)