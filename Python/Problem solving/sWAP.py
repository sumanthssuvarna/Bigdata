# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# For Example:

# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  

s="Sumanth"

s=list(s)
a=[]
for i in s:
  if i.isupper():
    a.append(i.lower())
  else:
    a.append(i.upper())
a="".join(a)
a