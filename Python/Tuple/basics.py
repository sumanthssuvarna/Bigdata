# **Tuple Questions:**

# 11. How do you create an empty tuple in Python?
a=()

# 12. Can you modify the elements of a tuple after it's created?
##No

# 13. How do you access elements in a tuple?
##By index

# 14. What is the purpose of using parentheses in tuple creation?
##Just to understand it is a tuple

# 15. How do you convert a list to a tuple and vice versa?
a=list(a)
a=tuple(a)
a

# 16. Explain the concept of unpacking a tuple.
list_of_tuples = [(1, 'one'), (2, 'two'), (3, 'three')]
for i,j in list_of_tuples:
  print(f"{j} : {i}")