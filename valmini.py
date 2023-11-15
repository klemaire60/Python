def minimum(tab : list) -> float:
    nbElements = len(tab)
    if(len(tab) == 0):
        return 0
    min = 0
    for i in range(nbElements):
        if(i == 0):
            min = tab[i]
        
        if(min > tab[i]):
            min = tab[i]

val = minimum([5, 2, 9, 4])
print(val)