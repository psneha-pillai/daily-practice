'''def squareroot(m,n):
    ans=-1
    for i in range(0,m+1):
        if(i**n==m):
            ans=i
        elif(i**n>m):
            break
    return ans
m=int(input())
n=int(input)
print(squareroot(m,n))'''

def squarerootbinary(m,n):
    low=1
    high=m
    while(low<=high):
        mid=(low+high)//2
        if(mid**n==m):
            return mid
        elif(mid**n>m):
            high=mid-1
        else:
            low=mid+1
    return -1
m=int(input())
n=int(input())
print(squarerootbinary(m,n))
