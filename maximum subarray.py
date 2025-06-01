def maxSubArray(nums):
    n=len(nums)
    maxsum=float("-inf")
    sum=0
    for i in nums:
        sum+=i
        maxsum=max(maxsum,sum)
        if(sum<0):
            sum=0
    return maxsum
nums=list(map(int,input().split()))
print(maxSubArray(nums))
