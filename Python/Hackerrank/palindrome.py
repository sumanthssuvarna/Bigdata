a="A man, a plan, a canal, Panama"

#make it lower case
a=a.replace(" ","").replace(",","").lower()

#Reverse it
b=a[::-1]

#Compare
if a==b:
#Output
  print("True")
else:
  print("Not a palindrome")

