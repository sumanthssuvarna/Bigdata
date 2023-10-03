# We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

# Let's try to understand this with an example.

# You are given an immutable string, and you want to make changes to it.

s="Aaaaaaa"
t="b"
p=2
a=list(s)
a[p]=t
b="".join(a)
b

# o/p

# Sample Input

# STDIN           Function
# -----           --------
# abracadabra     s = 'abracadabra'
# 5 k             position = 5, character = 'k'
# Sample Output

# abrackdabra