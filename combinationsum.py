'''amazon'''
'''method take donnt take'''
'''number can be tsken infinite nmbr of times'''
def genertate(ind,curr,ans,candidates,target):
    if (target==0):
        ans.append(curr.copy())
        return
    if(target<0 or ind==len(candidates)):
        return
    curr.append(candidates[ind])
    genertate(ind,curr,ans,candidates,target-candidates[ind]) '''(ind+1,curr ans candidate,target-candidates[ind])'''
    curr.pop()
    genertate(ind+1,curr,ans,candidates,target) '''for i in range (ind+1,len(candidates))'''
def combinationSum(candidates:list[int],target:int):'''if (candidates[ind]!=candidates[i])'''
    '''candidates.sort()'''
    ind=0
    curr=[]
    ans=[]
    genertate(ind,curr,ans,candidates,target)
    return ans
candidates=list(map(int,input().split()))
target=int(input("enter the target"))
print(combinationSum(candidates,target))