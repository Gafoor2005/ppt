l = [10,20,30,40,50]
a = int(input("enter index to insert : "))
b = int(input("enter element to insert: "))
# l.insert(a,b)
res = []
for i in range(len(l)):
    if(a == i):
        res.append(b)
        continue
    if(len(res)==i):
        res.append( l[i])
    else:
        res[i].append( l[i-1])
    print(i)
res.append( l[-1])
print(res)
