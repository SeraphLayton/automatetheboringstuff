import pyinputplus as pyip 

totalcost = 0
items = []

responseBread = pyip.inputMenu(['wheat', 'white', 'sourdough' ], prompt="Which bread u want?\n", numbered=True)
items.append('bread')

responseProtein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt="The Protein?\n", numbered=True)
items.append('protein')

responseCheese = pyip.inputYesNo(prompt="U wanna cheese?(Y/N)\n")
if responseCheese == 'yes':
    responseTypeCheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], prompt="What type of cheese?\n", numbered=True)
    items.append('cheese')

responseMayo = pyip.inputYesNo(prompt="Mayo?(Y/N)\n")
items.append('mayo')
responseMustard = pyip.inputYesNo(prompt="mustard?(Y/N)\n")
items.append('musatrd')
responseLettuce = pyip.inputYesNo(prompt="lettuce?(Y/N)\n")
items.append('lettuce')
responseTomato = pyip.inputYesNo(prompt="tomato?(Y/N)\n")
items.append('tomato')


totalcost = 0.5 * len(items)  # dollar per item

responseCount = pyip.inputInt(prompt="How many Sandwiches do u want?\n", blockRegexes=['[0|-|.]'])
totalcost = totalcost * responseCount


print("Ur sandwich(es) cost: " + str(totalcost) + "$")