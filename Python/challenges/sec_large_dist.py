# Second largest distinct number
a=[1,2,3,4,5,5,6,6,7,8,8]
b=[]
c=[]
d=[]

for i in a:
  if i not in b:
    b.append(i)
  else:
    c.append(i)

for i in b:
  if i in c:
    pass
  else:
    d.append(i)

d[-2]