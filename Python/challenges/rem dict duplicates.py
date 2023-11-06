#Remove duplicates inside the list of dictionaries

a=[{"name":"shiv","age":20},{"name":"ajith","age":21},{"name":"Sumanth","age":20},{"name":"shiv","age":20}]

for i in range(len(a)):
  if a.index(a[i])!=i:
    a.remove(a[i])
a
