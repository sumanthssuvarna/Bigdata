# We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

# Let's try to understand this with an example.

# You are given an immutable string, and you want to make changes to it.

def mutate_string(string, position, character):
    a=list(string)
    a[position]=character
    b="".join(a)
    return(b)


# o/p

# Sample Input

# STDIN           Function
# -----           --------
# abracadabra     s = 'abracadabra'
# 5 k             position = 5, character = 'k'
# Sample Output

# abrackdabra