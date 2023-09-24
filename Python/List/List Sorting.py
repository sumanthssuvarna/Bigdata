#8. **List Sorting:** Create a function that sorts a list of strings in alphabetical order without using built-in sorting functions.


a=['dsa','asg','bcd','asf']
n=len(a)

#bubble sort
for i in range(n):
  for j in range(n-1-i):
    if a[j]>a[j+1]:
      a[j],a[j+1]=a[j+1],a[j]

print(a)

#with builtin

a=['dsa','asg','bcd','asf']
set(a)