#to get avg in a list

def average(array):
    # your code goes here
    a=list(set(array))
    b=0
    for i in a:
        b=b+i
    return(b/len(a))

#OR

def average(array):
    return(sum(list(set(array)))/len(list(set(array))))