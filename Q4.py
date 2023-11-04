l = [10,20,20,30,25,10,30]
a = int(input("enter start index: "))
b = int(input("enter stop index: "))
res = []
for i in range(len(l)):
    if(i>=a and i<b):
        continue
    res.append(l[i])
print(res)