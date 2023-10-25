import random

card_data = []
card_list = [
    "P.E.K.K.A", 
    "Balloon", 
    "Witch", 
    "Golem", 
    "Prince", 
    "Giant Skeleton", 
    "Dark Prince", 
    "Three Musketeers", 
    "Baby Dragon", 
    "Skeleton Army", 
    "Hunter", 
    "Executioner", 
    "Bowler", 
    "Cannon Cart", 
    "Mega Knight", 
    "Wall Breakers", 
    "Goblin Giant", 
    "Electro Dragon", 
    "Raging Prince", 
    "Goblin Barrel", 
    "Mirror", 
    "Lightning", 
    "Poison", 
    "Graveyard", 
    "Tornado", 
    "Clone", 
    "Earthquake", 
    "Barbarian Barrel", 
    "Royal Delivery"
]

# Initialize jokes
def init():
    # setup jokes into a dictionary with id, joke, haha, boohoo
    item_id = 0
    for item in card_list:
        card_data.append({"id": item_id, "joke": item, "haha": 0, "boohoo": 0})
        item_id += 1
    # prime some haha responses
    for i in range(10):
        id = getRandomJoke()['id']
        addJokeHaHa(id)
    # prime some haha responses
    for i in range(5):
        id = getRandomJoke()['id']
        addJokeBooHoo(id)
        
# Return all jokes from jokes_data
def getJokes():
    return(card_data)

# Joke getter
def getJoke(id):
    return(card_data[id])

# Return random joke from jokes_data
def getRandomJoke():
    return(random.choice(card_data))

# Liked joke
def favoriteJoke():
    best = 0
    bestID = -1
    for joke in getJokes():
        if joke['haha'] > best:
            best = joke['haha']
            bestID = joke['id']
    return card_data[bestID]
    
# Jeered joke
def jeeredJoke():
    worst = 0
    worstID = -1
    for joke in getJokes():
        if joke['boohoo'] > worst:
            worst = joke['boohoo']
            worstID = joke['id']
    return card_data[worstID]

# Add to haha for requested id
def addJokeHaHa(id):
    card_data[id]['haha'] = card_data[id]['haha'] + 1
    return card_data[id]['haha']

# Add to boohoo for requested id
def addJokeBooHoo(id):
    card_data[id]['boohoo'] = card_data[id]['boohoo'] + 1
    return card_data[id]['boohoo']

# Pretty Print joke
def printJoke(joke):
    print(joke['id'], joke['joke'], "\n", "haha:", joke['haha'], "\n", "boohoo:", joke['boohoo'], "\n")

# Number of jokes
def countJokes():
    return len(card_data)

# Test Joke Model
if __name__ == "__main__": 
    init()  # initialize jokes
    
    # Most likes and most jeered
    best = favoriteJoke()
    print("Most liked", best['haha'])
    printJoke(best)
    worst = jeeredJoke()
    print("Most jeered", worst['boohoo'])
    printJoke(worst)
    
    # Random joke
    print("Random joke")
    printJoke(getRandomJoke())
    
    # Count of Jokes
    print("Jokes Count: " + str(countJokes()))