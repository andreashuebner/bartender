import random
questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}
ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

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

def mix_drinks(dictAnswers):
    listIngredients=[]
    for key in dictAnswers:
        if dictAnswers[key] == True:
            randomDrink=random.choice(ingredients[key])
            listIngredients.append(randomDrink)
            
    return listIngredients
        

if __name__ == "__main__":
   dictAnswers=ask_questions()
   mix_drinks(dictAnswers)