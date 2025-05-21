'''from math import *
def smallestdiv(arr,k):
    for div in range(1,max(arr)+1):
        sum=0
        for nums in arr:
            sum+=ceil(arr(div))
        if(sum<=k):
            return div
arr=list(map(int,input().split()))
k=int(input())
print(smallestdiv(arr,k))'''

from math import *
def smallestDivBin(arr,k):
    low=0
    high=max(arr)
    while(low<=high):
        div=(low+high)//2
        sum=0
        for nums in arr:
            sum+=ceil(nums/div)
        if(sum<=k):
            high=div-1
        else:
            low=div+1
    return low
arr=list(map(int,input().split()))
k=int(input())
print(smallestDivBin(arr,k))
