nums=list(map(int,input().split()))
def generate(ind,curr_arr,ans,nums):
    if(ind==len(nums)):
        ans.append(curr_arr.copy())
        return
    curr_arr.append(nums[ind])
    generate(ind+1,curr_arr,ans,nums)#take
    curr_arr.pop()
    generate(ind+1,curr_arr,ans,nums)
def subsets(nums):
    ind=0
    curr_arr=[]
    ans=[]
    generate(ind,curr_arr,ans,nums)
    return ans
print(subsets(nums))