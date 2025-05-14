lst=list(map(int,input().split()))
v=0
for i in range(len(lst)):
    if lst[i]%2!=0:
        temp=lst.pop(i)
        lst.insert(v,temp)
        v+=1
    print(lst)