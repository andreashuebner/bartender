import random
questions = { #All questions will be asked
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}
ingredients = { #Possible list of ingredients, one will be chosen at random for every taste confirmed by customer
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

listAdjectives=[] #will be populated with adjectives for naming coctails
listNouns=[] #will be populated with nouns for naming coctials
listAdjectives.append("fluffy")
listAdjectives.append("sweet")
listAdjectives.append("red")
listAdjectives.append("Irish")

listNouns.append("Martini")
listNouns.append("Sidecar")
listNouns.append("Rose")
listNouns.append("Manhattan")

'''Function that asks whether customer wants another drink.
@param {string} nameOfCustomer
@param {boolean} True if customer wants another drink, False if not
'''
def ask_for_other_drink(nameOfCustomer):
    answer=raw_input(nameOfCustomer + " , would you like another drink? (y/n)")
    answerLower=answer.lower()
    if answerLower.startswith("y"):
        return True
    else:
        return False
    
'''Asks and returns the name of customer
@returns {String} The name of the customer
'''
def get_name_of_customer():
    nameOfCustomer=raw_input("Please tell me your name: ")
    return nameOfCustomer
'''Function that chooses a random adjective and noun from the list of nouns/adjectives and returns a combined name of the drink
@return {string} - The name of the drink
'''
def get_name():
    randomAdjective = random.choice(listAdjectives)
    randomNoun = random.choice(listNouns)
    nameOfDrink = randomAdjective + " " + randomNoun
    return nameOfDrink


'''Asks how customer likes his/her drinks and returns a dict with attribute of ingredient
as key and True/False as value
@returns {dict} Dict with attributes like "strong, sweet" a key and boolean as value
'''
def ask_questions():
    dictAnswers={} #Will save either True or False for the questions asked
    for key in questions:
        answer=raw_input(questions[key] + " ")
        answerLower=answer.lower()
        if answerLower.startswith("y"):
            dictAnswers[key] = True
        else:
            dictAnswers[key] = False
            
    return dictAnswers
''' For every attribute in dictAnswers set to True, select a suitable ingredient at random
@param {dict} dictAnswers - Having the attribute of ingredient as key and boolen as value
@return {list] - Returns the list of randomly chosen suitable ingredients
'''
def mix_drinks(dictAnswers):
    listIngredients=[]
    for key in dictAnswers:
        if dictAnswers[key] == True:
            randomDrink=random.choice(ingredients[key])
            listIngredients.append(randomDrink)
            
    return listIngredients
        

if __name__ == "__main__":
   hasWishAnotherDrink = True
   while hasWishAnotherDrink == True:
       nameOfCustomer = get_name_of_customer()
       dictAnswers=ask_questions()
       mixedDrink=mix_drinks(dictAnswers)
       nameOfDrink=get_name()
       print (nameOfCustomer + ", here is your drink " + nameOfDrink + " with the ingredients " + str(mixedDrink))
       hasWishAnotherDrink=ask_for_other_drink(nameOfCustomer)