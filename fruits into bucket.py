'''
def fruitslen(fruits):
    n=len(fruits)
    maxlen=0
    for i in range(0,n):
        s=set()# after the break it will come to i loop and start fresh set
        for j in range(i,n):
            s.add(fruits[j])
            if(len(s)>2):
                break
            maxlen=max(maxlen,j-i+1)
    return maxlen
fruits=list(map(int,input().split()))
print(fruitslen(fruits))'''




def fruitslen(fruits):
    n=len(fruits)
    right=0
    left=0
    maxlen=0
    d={}
    while(right<n):
        if(fruits[right] in d):
            d[fruits[right]]+=1
        else:
            d[fruits[right]]=1
        if(len(d)>2):
            while(len(d)>2):
                d[fruits[left]]-=1
                if(d[fruits[left]]==0):
                   del d[fruits[left]]
                left+=1
        maxlen=max(maxlen,right-left+1)
        right+=1
    return maxlen
fruits=list(map(int,input().split()))
print(fruitslen(fruits))
