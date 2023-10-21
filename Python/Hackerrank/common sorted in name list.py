#input  "eefaggfahhs ashetty"
#output ['aefghs', 'aehsty']

a="eefaggfahhs ashetty"
a=a.split(" ")
p=[]
for i in a:
  q=[]
  for j  in i:
    q.append(j)
  q=p.append("".join(sorted(set(q))))


print(p)
