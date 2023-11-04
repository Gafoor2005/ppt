# first occurance
# replace first occurance with zero
l = [10,20,20,30,25,10,30]
a = int(input("enter element to remove: "))
for i in range(len(l)):
    if(a == l[i]):
        l[i] = 0
        break
print(l)