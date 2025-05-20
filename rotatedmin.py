def minrotated(arr):
    n=len(arr)
    low=0
    high=n-1
    Min=float("inf")
    while(low<=high):
        mid=(low+high)//2
        if(arr[low]<=arr[mid]):
            if(arr[low]<Min):
                Min=arr[low]
            low=mid+1
        if(arr[mid]<=arr[high]):
            if(arr[mid]<Min):
                Min=arr[mid]
            high=mid-1
    return Min
arr=list(map(int,input().split()))
print(minrotated(arr))
              



def countrotation(arr):
    n=len(arr)
    low=0
    high=n-1
    Min=float("inf")
    minInx=-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[low]<=arr[mid]):
            if(arr[low]<Min):
                Min=arr[low]
                minInx=low
            low=mid+1
        if(arr[mid]<=arr[high]):
            if(arr[mid]<Min):
                Min=arr[mid]
                minInx=mid
            high=mid-1
    return minInx
arr=list(map(int,input().split()))
print(countrotation(arr))
              
