def QuestionsMarks(s):
  qnum = 0
  dig = 0
  has_10 = False
  for ch in s:
    if ch.isdigit():
      if int(ch) + dig == 10:
        if qnum != 3:
          return 'false'
        has_10 = True
      dig = int(ch)
      qnum = 0
    elif ch == '?':
      qnum += 1
  return 'true' if has_10 else 'false'
  
print(QuestionsMarks("arrb6???4xxbl5???eee5")) # True
print(QuestionsMarks("acc?7??sss?3rr1??????5")) # True
print(QuestionsMarks("5??aaaaaaaaaaaaaaaaaaa?5?5")) # False
print(QuestionsMarks("9???1???9???1???9")) # True
print(QuestionsMarks("aa6?9")) # False