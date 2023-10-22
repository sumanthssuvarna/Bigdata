a="This is a test. This test is a test."
a=a.replace(".","").lower().split()

b={}
for i in a:
  if i in b:
    b[i]=b[i]+1
  else:
    b[i]=1

print(b)
