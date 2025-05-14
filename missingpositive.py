lst=list(map(int,input().split()))
for i in range(1
               ,len(lst)+2):
    if i not in lst:
        lst.append(i)
        lst.sort()
    print(lst)
                
