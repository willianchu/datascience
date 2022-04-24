# Questions Marks
# Have the function Questions_Marks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. If so, then your program should return the string true, otherwise it should return the string false. If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

# For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.

   
# remove letters from the string except for numbers and question marks
def remove_letters(string):
  without_letters = ""
  for char in string:
    if char.isdigit() or char == "?":
      without_letters += char
  return without_letters

def Questions_Marks(strParam):
  numbers_and_question_marks = remove_letters(strParam)
  found = False
  for i in range(0, len(numbers_and_question_marks) - 4):
    if numbers_and_question_marks[i].isdigit() and numbers_and_question_marks[i+4].isdigit():
      if numbers_and_question_marks[i+1] == "?" and numbers_and_question_marks[i+2] == "?" and numbers_and_question_marks[i+3] == "?" and (int(numbers_and_question_marks[i]) + int(numbers_and_question_marks[i+4])) == 10:
        found = True

  return found



  # keep this function call here 
print(Questions_Marks("arrb6???4xxbl5???eee5")) # True
print(Questions_Marks("acc?7??sss?3rr1??????5")) # True
print(Questions_Marks("5??aaaaaaaaaaaaaaaaaaa?5?5")) # False
print(Questions_Marks("9???1???9???1???9")) # True
print(Questions_Marks("aa6?9")) # False

