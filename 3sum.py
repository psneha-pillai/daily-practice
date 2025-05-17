'''s=set()'''
'''s={0}'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet_sum=set()
        n=len(nums)
        for i in range(0,n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if(nums[i]+nums[j]+nums[k]==0):
                        temp=[nums[i]+nums[j]+nums[k]]
                        temp.sort()
                        triplet_sum.add(tuple(temp))
        ans=[]
        for triple in triplet_sum:
            ans.append(list(triple))
            return ans
''' hashing
i+j+k=0
k=-(i+j)'''
 class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet_sum=set()
        n=len(nums)
        for i in range(0,n-1):
            hashmap=[]
            for j in range(i+1,n):
                k=-(num[i]+num[j])
            if(k in hashmap):
                temp=[nums[i],nums[j],k]
                temp.sort()
                triplet_sum.add(tuple(temp))
                hasmap.append(nums[j])
        ans=[]
        for triple in triple_sum:
            ans.append(list(triple))
        return ans

    class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        nums.sort()
        for i in range(0,n):#number -2
            if i>0 and nums[i]==nums[i+1]:# 1>o and nums[i]=-2==-2
                continue
            j=i+1
            k=n-1
            while j<k:
                sum=nums[i]+sum[j]+nums[k]
                if sum<0:
                    j+=1
                elif sum>0:
                    k-=1
                else:
                    temp[num[i],num[j],nums[k]]
                    ans.append(temp)
                    j+=1
                    k-=1
                    while(j<k and nums[j-1]=nums[j]):#to jump into othre number with is no commen to j or i or k
                        k-=1
                return ans    
