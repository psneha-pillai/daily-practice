l1=list(map(input().split()))
s=input()
index=0
while len(l1)==len(s):
    i=0
    for i in range(0,len(l1)):
        if i==s[index]:
            return True
        
