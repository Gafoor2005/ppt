# differences of list
l = [10,54,92,68,65,4,89,23]
l2 = [10,54,65,24,4,89,44]
dif = []
for e in l+l2:
    if((e not in l)or(e not in l2)) and (e not in dif):
        dif += [e]
print('differences is ',dif)