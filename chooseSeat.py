layout = [
    ["O","e","e",None, "e","o","e",None, "o","o","E"], # row 1
    ["O","o","e",None, "e","o","e",None, "e","o","E"], # row 2
    ["O","o","o",None, "o","o","e",None, "o","e","O"], # row 3
    ["E","o","e",None, "e","o","e",None, "o","e","E"], # row 4 [3,-1]
    ["E","e","o",None, "e","e","e",None, "o","o","E"], # row 5 [4,0]
    ["O","e","e",None, "e","e","e",None, "e","e","E"]  # row 6 [5,-1]
]

def findWindowSeat(layout):
  line = 0
  for row in layout:
    # right place
    if row[-1] == "E" and row[-2] == "e": 
      return (line, -1); # return the line at the first seat
    line += 1
  return None

print(findWindowSeat(layout))