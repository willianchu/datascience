# dictionary where 
landmarks = {
    "Big Ben": 12,
    "Tower Bridge": 25,
    "Buckingham Palace": 15,
    "Madame Tussauds": 25,
    "London Eye": 40,
    "Tower of London": 25,
    "Emirates Air Line cable car": 16,
    "London Transport Museum": 7,
    "Wembley Stadium": 8,
    "Hyde Park": 0,
    "The View from The Shard": 14
}

def lessThanFifteenMinutes(landmark):
    return landmarks[landmark] < 15

def quickList(landmarks):
    newList = []
    for element in landmarks:
        if lessThanFifteenMinutes(element):
            newList.append(element)
    return newList

newList = quickList(landmarks)
print (newList)
print (len(newList))



