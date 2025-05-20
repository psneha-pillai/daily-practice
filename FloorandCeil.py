def getFloorCeil(a,n,x):
    def getFloor(a,n,X):
        low=0
        n=len(a)
        high=n-1
        ans=-1
        while(low<=high):
            mid=(low+high)//2
            if(a[mid]<=x):
                ans=a[mid]
                low=mid+1
            else:
                high=mid-1
        return ans
    def getCeil(a,n ,x):
        low=0
        high=n-1
        ans=-1
        while(low<=high):
            mid=(low+high)//2
            if(a[mid]>x):
                ans=a[mid]
                high=mid-1
            else:
                low=mid+1
        return ans
    a.sort()
    floor=getFloor(a,n,x)
    ceil=getCeil(a,n,x)
    return[floor,ceil]
a=list(map(int,input().split()))
n=len(a)
x=int(input())
print(getFloorCeil(a,n,x))
