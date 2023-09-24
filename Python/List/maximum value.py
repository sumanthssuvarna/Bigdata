#2. **Find the Maximum Value:** Create a function to find the maximum value in a list of numbers without using built-in functions like `max()`.

a=[6, 7, 4, 3, 3]
large=None

for i in a:
  if large is None or large<i:
    large=i

print(large)

#OR

a=[6, 7, 4, 3, 3]
large=0

for i in a:
  if large<i:
    large=i

print(large)

#using built-in function

a=[6, 7, 4, 3, 3]
max(a)