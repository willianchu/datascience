starters = {
    "Potato Pancakes": 7.99,
    "Salami Platter": 10.29,
    "Brezel": 6.99,
    "Maultaschen": 9.99,
    "Fried Potatoes": 4.99
}

mains = {
    "Braised Beef Short Ribs": 18.99,
    "Paprika Beef Goulash": 15.5,
    "Jager Schnitzel": 16.99,
    "House-mase Bratwurst": 11.99,
    "Kasespatzle": 14.99,
    "German Ravioli": 12.79,
    "Curry Wurst": 10.99
}

desserts = {
    "Chilled Chocolate Fondant": 7.9,
    "Pepermint Crisp Tart": 5.9,
    "Ginger Cobbler": 6.9,
    
}

beers = {
    "Stigel Radler": 6.9,
    "Munich Lager": 7.9,
    "Kong Ludwig Weissbier": 8.9,
    "Warsteiner Punkel": 7.5,
}

# if you want to see the keys of the dictionary in the list: keys = list(starters.keys())
# if you want to see the keys of the dictionary in the list: values = list(starters.values())
import json

def mostExpensiveKey(dictionary):
  # return the key of the most expensive dish option in the dictionary
  return max(dictionary, key=dictionary.get) 

def dotsMenu():
  # the names of the courses as the keys (starters, mains...), and the name of the food or drink item as the values for new dict meals.
  coursesSelected = {}
  coursesSelected["starters"] = {mostExpensiveKey(starters) : starters[mostExpensiveKey(starters)]}
  coursesSelected["mains"] = {mostExpensiveKey(mains) : mains[mostExpensiveKey(mains)]}
  coursesSelected["desserts"] = {mostExpensiveKey(desserts) : desserts[mostExpensiveKey(desserts)]}
  coursesSelected["beers"] = {mostExpensiveKey(beers) : beers[mostExpensiveKey(beers)]}
  return coursesSelected

def menuTotal(order):
  total = 0
  for course in order:
    for dish in order[course]:
      total += order[course][dish]
  return total

def tip10Percent(total): #  Dot gives a 10% tip on this meal
  return total * 0.1

meals = dotsMenu() # Create a new dictionary called meals
pretty = json.dumps(meals, indent=2) # Print the dictionary in a pretty format
print(pretty)
print("Total:", menuTotal(meals))
print("10% Tip:", tip10Percent(menuTotal(meals)))