import random
import json

card_data = []

# Initialize cards
def initCards():
    global card_data
    try:
        with open("carddb.json", "r") as file:
            card_data = json.load(file)
        print("Successfully loaded JSON data:", card_data)
    except FileNotFoundError:
        card_data = []
        print("File not found.")
    except Exception as e:
        print("Error:", e)
  # Initialize an empty list if the file is not found

# Call initCards() to load the card data from carddb.json
initCards()

def getCard():
    return(card_data)

# Define the getCard function
def getCard(id):
    for card in card_data:
        if card["id"] == id:
            return card
        
# Generate a random card
def generateRandomCard():
    print(card_data)  # Add this line to check the contents of card_data
    return random.choice(card_data)

# Number of cards
def countCards():
    return len(card_data)

# Test Card Model
if __name__ == "__main__":

    # Random card
    print("Random card:")
    random_card = generateRandomCard()
    print(random_card)

