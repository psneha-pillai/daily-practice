def slinding_window_fixed(arr,k):
    if(len(arr)<k):
        return -1
    window_sum=sum(arr[:k])
    max_sum=window_sum
    for i in range(1,len(arr)):
        window_sum+=arr[i]-arr[i-k]
        max_sum=max(max_sum,window_sum)
    return max_sum
arr=list(map(int,input().split()))
k=int(input("enter:"))
print(slinding_window_fixed(arr,k))