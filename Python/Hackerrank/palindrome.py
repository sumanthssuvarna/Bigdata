a="A man, a plan, a canal, Panama"
a=a.replace(" ","")
a=a.replace(",","")
b=a
a=a.upper()
b=b.upper()
b=b[::-1]
print(a)
print(b)
if a==b:
  print("True")
else: 
  print("False")

