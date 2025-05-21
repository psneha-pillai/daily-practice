'''from math import *
def KokoEat(arr,k):
    for noofBanana in range(1,max(arr)):
        time=0
        for nums in arr:
            time+=ceil(nums/noofBanana)
        if(time<=k):
            return noofBanana
arr=list(map(int,input().split()))
k=int(input())
print(KokoEat(arr,k))'''

from math import *
def kokofind(arr,k):
    low=1
    high=max(arr)
    while(low<=high):
        noofbanana=(low+high)//2
        time=0
        for nums in arr:
            time+=ceil(nums/noofbanana)
        if(time<=k):
            high=noofbanana-1
        else:
            low=noofbanana+1
    return low
arr=list(map(int,input().split()))
k=int(input())           
print(kokofind(arr,k))
