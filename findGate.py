WIDE_BODY = "W"	

def is_available(gate):
  return gate.isupper()

def wide_Body(element):
  if element.lower() == "wide":
    size_compare = WIDE_BODY
  else:
    size_compare = element
  return size_compare == WIDE_BODY

def find_the_gate(spots, vehicle):
    for gate in spots:
      if is_available(gate):
        if not wide_Body(vehicle):
          return spots.index(gate)
        elif wide_Body(gate):
          return spots.index(gate)
    return False
          

print(find_the_gate(
  ['w','n','N'], 'narrow'
))

print(find_the_gate(
  ['w','n','N','W','n','W'],'wide'
))

print(find_the_gate(
  ['w','n','n','w','n','n'], 'narrow'
))

print(find_the_gate(
  ['w','n','n','w','N','n','w','N','N','w','n','n','w','n','n','W','W','W','W','n','n','w','n','n'], 'wide'
))