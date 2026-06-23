class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        s=0
        k=0
        for i,j in d.items():
            if j>s:
                s=j
                k=i
        return k