# sort in ascending or descending
l = [10,20,20,30,25,10,30]
for j in range(len(l)-1):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            t = l[i]
            l[i] = l[i+1]
            l[i+1] = t
print('asce is :')
for i in l:
    print(i,end=' ')
print()
print('desc is :')
for i in range(len(l)):
    print(l[-i-1] , end=' ')
print()