def longest_substring_slidingwindow(arr,target):
    left=0
    curr_sum=0
    max_len=0
    for right in range(len(arr)):
        curr_sum+=arr[right]
    while curr_sum>target:
        curr_sum-=arr[left]
        left+=1
    max_len=max(max_len,right-left+1)
    return max_len
arr=list(map(int,input().split()))
target=int(input())
print(longest_substring_slidingwindow(arr,target))
