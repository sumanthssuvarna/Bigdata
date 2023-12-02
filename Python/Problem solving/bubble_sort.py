a=[1, 22, 3,77, 4, 5, 6,0, 7, 8, 9, 10]
for i in range(len(a)):
  for i in range(len(a)-1):
    if a[i]>a[i+1]:
      temp=a[i]
      a[i]=a[i+1]
      a[i+1]=temp

a
