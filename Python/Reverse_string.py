# Reverse a string without pre-build function

a="abc"
b=""
for i in a:
  b=b+i
print(b)

# OR

a="abc"
b=a[::-1]
print(b)

# Reverse a string with pre-build function

a="abd"
b="".join(reversed(a))
print(b)