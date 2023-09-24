a="Sumanth"
b="Suvarna"
c="Apple,Orange,Banana"
d="    Laaalaalaa   "


# 1. Concatenate two strings together.
Concatenate=a+" "+b
print(Concatenate)
          #OR
Concatenate=",".join([a,b])
print(Concatenate)

# 2. Find the length (number of characters) of a string.
lenght=len(a)
print(lenght)

# 3. Extract a portion of a string using slicing.
sliced=a[0:3]
print(sliced)

# 4. Split a string into a list of substrings based on a delimiter.
splitt=c.split(",")
print(splitt)

# 5. Remove leading and trailing whitespace (or specific characters) from a string
print(d) #Before strip
space_rem=d.strip(" ")
print(space_rem)

# 6. Convert a string to uppercase or lowercase.
upp=a.upper()
low=a.lower()
print(upp," ",low)

# 7. Replace occurrences of a substring within a string.
updated=c.replace("Apple","Kiwi")
print(updated)

# 8. Check if a substring exists within a string.
if "Banan" in c:
  print("Banana is there")

# 9. Format strings using f-strings or the `.format()` method.
print(f"First name : {a} Second name : {b}")
     #OR
print("First name : {} Second name is: {}".format(a,b))

# 10. Reverse a string.
rev1=a[::-1]
print(rev1)
  #OR
e=""
for i in a:
  e=i+e
print(e)