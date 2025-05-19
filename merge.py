def mergeSort(arr,n):
    def ms(arr,low,high):
        if(low==high):
            return
        mid=(low+high)//2
        ms(arr,low,mid)
        ms(arr,mid+1,high)
        Sort(arr,low,mid,high)
    def Sort(arr,low,mid,high):
        i=low
        j=mid+1
        k=[]
        while (i<=mid and j<=high):
            if(arr[i]<=arr[j]):
                k.append(arr[i])
                i+=1
            else:
                k.append(arr[j])
                j+=1
        while(i<=mid):
            k.append(arr[i])
            i+=1
        while(j<=high):
            k.append(arr[j])
            j+=1
        for ind,val in enumerate(k):
            arr[ind+low]=val
    low=0
    high=n-1
    ms(arr,low,high)
    return arr
arr = list(map(int,input().split()))
mergeSort(arr,len(arr))
print(arr)
