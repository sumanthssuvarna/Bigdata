# List methods
a=[1,2,3,4,5,6,11,11,7,8,9]
aa=[166,43,11,11,7,8,9]

#Program to find the length of a list
len(a)

#Program to add an element to a list
a.append(10)
#or
a.insert(4,11)

#Program to remove an element from a list
a.remove(11)

#Program to sort a list
a.sort()

#Program to reverse a list
a.sort(reverse=True)

#Program to find the maximum element in a list
b=max(a)
b

#Program to find the minimum element in a list
b=min(a)
b

#Program to check if an element exists in a list
if 2 in a:
  pass

#Program to merge two lists
b=a+a

#Program to find the intersection of two lists
list(set(a) & set(aa))

#Program to find the difference of two lists
list(set(a) - set(aa))

#Program to find the union of two lists
b=a+a

# 1. How do you create an empty list in Python?
a=[]

# 2. How do you add an element to the end of a list?
b=10
for i in range(b):
  a.append(i)

# 3. How do you remove an element from a list?
c=5
for i in range(c):
  a.remove(i)

# 4. How do you check if an element is in a list?
if 5 in a: pass
else: print()

# 5. Explain the difference between `append()` and `extend()` methods for lists.
d=["abc",3]
a.extend(d)

# 6. How do you find the length of a list?
e=len(a)

# 7. What is list slicing, and how is it done?
g=[1,2,5,4,3,6,7]
f=g[3:6]

# 8. How do you reverse a list in-place?
g.reverse() #or
i=d[::-1]

# 9. How do you sort a list in ascending order?
h=list(set(g)) #or
j=g.sort(reverse=True)

# 10. Explain the difference between `remove()` and `pop()` methods for removing elements from a list.
g.pop() #Remove last element
g.remove(4) #Remove prticulr element
