def lowerBound(arr,target):
    n=len(arr)
    low=0
    high=n-1
    ans=n
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>=target):
            ans=mid
            high=mid-1
        else:
             low=mid+1
    return ans
arr=list(map(int,input().split()))
target=int(input())
print(lowerBound(arr,target))
# if there are duplication in the arr it will give the smallest index
#if the target is not presebt in the the arr it will it will retuen len of the arr
