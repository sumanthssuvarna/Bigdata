# Sample Input:  chris alan

# Sample Output:  Chris Alan

def solve(s):
    s=s.split(" ")
    return(" ".join(i.capitalize() for i in s))