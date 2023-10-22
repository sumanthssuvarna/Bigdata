# Output Format

# Output the symmetric difference integers in ascending order, one per line.

# Sample Input

# STDIN       Function
# -----       --------
# 4           set a size M = 4
# 2 4 5 9     a = {2, 4, 5, 9}
# 4           set b size N = 4
# 2 4 11 12   b = {2, 4, 11, 12}
# Sample Output

# 5
# 9
# 11
# 12

import sys
inp = sys.stdin.read().splitlines()
a = set(map(int, (inp[1].split())))
b = set(map(int, (inp[3].split())))

c=a.union(b)-a.intersection(b)
d=sorted(list(c))
for i in d:
    print(i)

#or

for i in sorted(list(a.union(b)-a.intersection(b))):
    print(i)