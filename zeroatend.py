lst = list(map(int,input("enter").split()))
evens = []
odd=[]
for i in lst:
    if i % 2 == 0:
        evens.append(i)
    else:
        odd.append(i)
lst=evens+odd
print(lst)

 
'''for i in list:
if i%2==0:
    list.append(i)
    list.remove(i)
    print(lst)'''
''' '''