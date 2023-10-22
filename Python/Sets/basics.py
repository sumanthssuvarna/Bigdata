# **Set Questions:**

# 17. How do you create an empty set in Python?
a={1,2}
a

# 18. What is the main characteristic of a set in terms of element uniqueness?
## remove duplicates & sort in ascending order

# 19. How do you add an element to a set?
a.add(4)
a

# 20. How do you remove an element from a set?
a.remove(4)
a

# 21. How do you perform set intersection and set union operations?
b={7,8,9}
a.intersection(b) #gives common between a and b
a.union(b) # Gives all values of aand b

# 22. Can sets contain other sets or mutable objects like lists?
##sets can only contain immutable objects as their elements. Immutable objects are objects whose values cannot be changed after they are created. 

# 23. Explain the purpose of using sets in Python.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2     # Union: {1, 2, 3, 4, 5}
intersection_set = set1 & set2  # Intersection: {3}
difference_set = set1 - set2    # Difference: {1, 2}